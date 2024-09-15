"""
Main route file
"""
import os
import logging
import tempfile
from typing import Any
from fastapi.responses import FileResponse, HTMLResponse
from fastapi import (
    FastAPI,
    Request,
    File,
    UploadFile,
    Form,
    HTTPException,
)
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from .api.rm_bg import Remover
from .api.heic2jpg import Converter
from .api.make_qr import QRCodeGenerator
from .api.email_sender_new.src.sender import AutoMailSender


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


def prefix_url(url: str) -> str:
    """
    Prefix the URL with the app's base url
    """
    if os.getenv('ENV') == "production":
        return f'/tool-box{url}'
    return url

def url_for_prefixed(request: Request, name: str, **path_params: Any) -> str:
    """
    Generate a URL for the given endpoint
    """
    if name == 'static':
        filename = path_params.get('filename', '')
        if filename:
            url = request.url_for('static', path=filename)
            return prefix_url(str(url))

    url = request.url_for(name, **path_params)
    return prefix_url(str(url))


templates.env.globals['url_for_prefixed'] = url_for_prefixed
users = {
    'user1': {
        'password': 'password1'
    },
    'user2': {
        'password': 'password2'
    }
}


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


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/about', response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


# @app.get('/log_in', response_class=HTMLResponse)
# async def login_page(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request})


# @app.get('/sign_up', response_class=HTMLResponse)
# async def signup_page(request: Request):
#     return templates.TemplateResponse("signup.html", {"request": request})


@app.get('/img_proc', response_class=HTMLResponse, name="img_proc")
async def img_proc(request: Request):
    return templates.TemplateResponse("img_proc.html", {"request": request})


@app.get('/email_sender', response_class=HTMLResponse)
async def email_sender(request: Request):
    return templates.TemplateResponse("email_sender.html", {"request": request})


@app.get('/email_temp', response_class=HTMLResponse)
async def email_temp(request: Request):
    return templates.TemplateResponse("email_temp.html", {"request": request})


@app.get('/contact', response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})


@app.post('/remove_background')
async def remove_background(image: UploadFile = File(...)):
    """
    Upload image and remove background
    """
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

    finally:
        if 'temp_filename' in locals():
            try:
                os.remove(temp_filename)
                logging.info("Temp file removed: %s", temp_filename)

            except ValueError:
                logging.error("Error removing temp file: %s", ValueError)


@app.post('/heic2jpg')
async def heic2jpg(url: str = Form(...)):  # Need to transfer to UploadFile
    """
    Convert HEIC image to another image format
    """
    try:
        converter = Converter(url)
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

    finally:
        if 'temp_filename' in locals():
            try:
                os.remove(temp_filename)
                logging.info("Temp file removed: %s", temp_filename)

            except ValueError:
                logging.error("Error removing temp file: %s", ValueError)


@app.post('/generate_qrcode')
async def generate_qrcode(url: str = Form(...)):
    """
    Generate QR code based on the input URL
    """
    try:
        generator = QRCodeGenerator(url)
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

    finally:
        if 'temp_filename' in locals():
            try:
                os.remove(temp_filename)
                logging.info("Temp file removed: %s", temp_filename)

            except ValueError:
                logging.error("Error removing temp file: %s", ValueError)


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
