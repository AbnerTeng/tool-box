"""
Main route file
"""
import os
import logging
from flask import (
    Flask,
    request,
    render_template,
    send_file,
    send_from_directory
)
from scripts.rm_bg import Remover
from scripts.make_qr import QRCodeGenerator
from scripts.email_sender.src.sender import AutoMailSender


app = Flask(__name__)
DOWNLOAD_FOLDER = '~/Desktop' # TODO: need revise
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

@app.route('/')
def home():
    """
    Home page
    """
    return render_template('index.html')

@app.route('/about')
def about():
    """
    About page
    """
    return render_template('about.html')

@app.route('/services')
def services():
    """
    Services page
    """
    return render_template('services.html')

@app.route('/contact')
def contact():
    """
    Contact page
    """
    return render_template('contact.html')

@app.route('/email_instructions')
def email_instructions():
    """
    Email instructions page
    """
    return render_template('email_instructions.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    """
    Function to serve static files
    """
    return send_from_directory('static', filename)


@app.route('/remove_background', methods=['POST'])
def remove_background():
    """
    Upload image and remove background
    """
    image_file = request.files['image']
    remover = Remover(image_file)
    output = remover.remove_bg()
    temp_file = os.path.join(app.config['DOWNLOAD_FOLDER'], 'download.png')
    output.save(temp_file)
    logging.info("Temp file saved: %s", temp_file)
    return send_file(temp_file, as_attachment=True)

@app.route('/generate_qrcode', methods=['POST'])
def generate_qrcode():
    """
    Generate QR code based on the input URL
    """
    url = request.form['url']
    generator = QRCodeGenerator(url)
    output = generator.get_qrcode()
    temp_file = os.path.join(app.config['DOWNLOAD_FOLDER'], 'download.png')
    output.save(temp_file)
    logging.info("Temp file saved: %s", temp_file)
    return send_file(temp_file, as_attachment=True)

@app.route('/send_email', methods=['POST'])
def send_email():
    """
    Send email based on sepcific templates
    """
    event = request.form['event']
    receiver_data = request.files['receiver']
    mail, passwords = request.form['email'], request.form['password']
    mail_sender = AutoMailSender(event, receiver_data, mail, passwords)
    date, __time__, name, mt_link, email = mail_sender.get_data()
    mail_sender.send_mail(date, __time__, name, mt_link, email)
    logging.info("Email sent successfully")
