"""
Main route file
"""
from typing import Dict, Union
import logging
import tempfile
from fastapi.responses import FileResponse
from fastapi import (
    FastAPI,
    File,
    UploadFile,
    Form,  # extract data from submission
    HTTPException,
)
from pydantic import AnyUrl, BaseModel, EmailStr

from app.api.rm_bg import Remover
from app.api.heic2jpg import Converter
from app.api.make_qr import QRCodeGenerator
from app.api.email_sender_new.src.sender import AutoMailSender
from app.api.mail_sender import send_mail

app = FastAPI()


class EmailRequest(BaseModel):
    """
    Email sender request model
    """
    event: str = Form(...)
    receiver_data: UploadFile = File(...)
    link: str = Form(...)
    subject: str = Form(...)
    email: str = Form(...)
    password: str = Form(...)


class URLRequest(BaseModel):
    """
    URL request model
    """
    url: AnyUrl = Form(...)


class ContactForm(BaseModel):
    """
    contact us form model
    """
    name: str = Form(...)
    email: EmailStr = Form(...)
    type_of_issue: str = Form(...)
    message: str = Form(...)


@app.post('/remove_background')
async def remove_background(image: UploadFile = File(...)):
    """
    Upload image and remove background
    """
    temp_filename = None
    try:
        remover = Remover(image.file)
        output = remover.remove_bg()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
            temp_filename = temp_file.name
            output.save(temp_filename)
            logging.info("Temp file saved: %s", temp_filename)

        return FileResponse(
            temp_filename,
            media_type="image/png",
            filename="background_removed.png",
        )

    except Exception as e:
        logging.error("Error removing background: %s", str(e))
        return HTTPException(status_code=500, detail="Error removing background")


@app.post('/heic2jpg')
async def heic2jpg(image: UploadFile = File(...)):
    """
    Convert HEIC image to another image format
    """
    try:
        converter = Converter(image.file)
        output = converter.heic2jpg()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_filename = temp_file.name
            output.save(temp_filename)
            logging.info("Temp file saved: %s", temp_filename)

        return FileResponse(
            temp_filename,
            media_type="image/jpg",
            filename="converted.jpg",
        )

    except Exception as e:
        logging.error("Error converting image: %s", str(e))
        return HTTPException(status_code=500, detail="Error converting image")


@app.post('/generate_qrcode')
async def generate_qrcode(request: URLRequest):
    """
    Generate QR code based on the input URL
    """
    temp_filename = None
    try:
        generator = QRCodeGenerator(**request.dict())
        output = generator.get_qrcode()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
            temp_filename = temp_file.name
            output.save(temp_filename)
            logging.info("Temp file saved: %s", temp_filename)

        return FileResponse(
            temp_filename,
            media_type="image/png",
            filename="qrcode.png",
        )

    except Exception as e:
        logging.error("Error generating QR code: %s", str(e))
        return HTTPException(status_code=500, detail="Error generating QR code")


@app.post('/send_email')
def send_email(request: EmailRequest):
    """
    Send email based on sepcific templates
    """
    try:
        mail_sender = AutoMailSender(**request.dict())
        infos = mail_sender.get_data()
        mail_sender.send_mail(infos)
        logging.info("Email sent successfully")
        return {"message": "Email sent successfully"}

    except Exception as e:
        logging.error("Error sending email: %s", str(e))
        return HTTPException(status_code=500, detail="Error sending email")


@app.post('/contact_us')
def send_contact_us_form(request: ContactForm):
    """
    send email to the admin based on contact us form
    """
    try:
        send_mail(request.dict())
        return {"message": "Email sent successfully"}

    except Exception as e:
        logging.error("Error sending email: %s", str(e))
        return HTTPException(status_code=500, detail="Error sending email")
