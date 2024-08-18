"""
Main route file
"""
import os
import logging
import tempfile
from flask import (
    Flask,
    request,
    render_template,
    send_file,
    send_from_directory,
    url_for,
    # Response
)
from scripts.rm_bg import Remover
from scripts.heic2jpg import Converter
from scripts.make_qr import QRCodeGenerator
from scripts.email_sender_new.src.sender import AutoMailSender


app = Flask(
    __name__,
    static_folder='app/static',
    template_folder='.'
)

app.jinja_loader.searchpath.append('app/templates')
# DOWNLOAD_FOLDER = '~/Desktop'
# app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER


def prefix_url(url: str) -> str:
    """
    Prefix the URL with the app's base url
    """
    if app.config.get('ENV') == "production":
        return f'/tool-box{url}'
    return url

def url_for_prefixed(endpoint, **values) -> str:
    """
    Generate a URL for the given endpoint
    """
    if endpoint == 'static':
        filename = values.get('filename', '')
        if filename:
            return prefix_url(f'/static/{filename}')

    return prefix_url(url_for(endpoint, **values))


app.jinja_env.globals['url_for_prefixed'] = url_for_prefixed
users = {
    'user1': {
        'password': 'password1'
    },
    'user2': {
        'password': 'password2'
    }
}

@app.route('/')
def home():
    """
    Home page
    """
    return render_template('index.html')

# @app.route('/login', methods=['POST'])
# def login():
#     """
#     Login page
#     """
#     data = request.json
#     username = data.get('username')
#     password = data.get('password')

#     if username in users and users[username]['password'] == password:
#         return jsonify({'message': 'Login successful'})
#     else:
#         return jsonify({'message': 'Invalid username or password'}), 401

# @app.route('/signup', methods=['POST'])
# def signup():
#     """
#     Signup page
#     """
#     data = request.json
#     username = data.get('username')
#     password = data.get('password')

#     if username in users:
#         return jsonify({'message': 'Username already exists'}), 400
#     else:
#         users[username] = {'password': password}
#         return jsonify({'message': 'Sign up successful'})

@app.route('/about_us.html')
def about():
    """
    About page
    """
    return render_template('about.html')


@app.route('/log_in.html', methods=['GET'])
def login_page():
    """
    Serve the login page
    """
    return render_template('login.html')


@app.route('/sign_up.html', methods=['GET'])
def signup_page():
    """
    Serve the signup page
    """
    return render_template('signup.html')


@app.route('/service1.html')
def img_proc():
    """
    Image processing page
    """
    return render_template('img_proc.html')


@app.route('/service2.html')
def email_sender():
    """
    Email sender page
    """
    return render_template('email_sender.html')


@app.route('/service2_templates.html')
def email_temp():
    """
    Email template page
    """
    return render_template('email_temp.html')


@app.route('/contact_us.html')
def contact():
    """
    Contact page
    """
    return render_template('contact.html')


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
    try:
        image_file = request.files['image']
        remover = Remover(image_file)
        output = remover.remove_bg()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
            temp_filename = temp_file.name
            output.save(temp_filename)
            logging.info("Temp file saved: %s", temp_filename)

        return send_file(
            temp_filename,
            as_attachment=True,
            download_name="background_removed.png",
        ), 200

    except ValueError:
        logging.error("Error removing background: %s", ValueError)
        return "Error removing background", 500

    finally:
        if 'temp_filename' in locals():
            try:
                os.remove(temp_filename)
                logging.info("Temp file removed: %s", temp_filename)

            except ValueError:
                logging.error("Error removing temp file: %s", ValueError)


@app.route('/heic2jpg', methods=['POST'])
def heic2jpg():
    """
    Convert HEIC image to another image format
    """
    try:
        url = request.form['url']
        converter = Converter(url)
        output = converter.heic2jpg()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_filename = temp_file.name
            output.save(temp_filename)
            logging.info("Temp file saved: %s", temp_filename)

        return send_file(
            temp_filename,
            as_attachment=True,
            download_name="converted.jpg",
        ), 200

    except ValueError:
        logging.error("Error converting image: %s", ValueError)
        return "Error converting image", 500

    finally:
        if 'temp_filename' in locals():
            try:
                os.remove(temp_filename)
                logging.info("Temp file removed: %s", temp_filename)

            except ValueError:
                logging.error("Error removing temp file: %s", ValueError)


@app.route('/generate_qrcode', methods=['POST'])
def generate_qrcode():
    """
    Generate QR code based on the input URL
    """
    try:
        url = request.form['url']
        generator = QRCodeGenerator(url)
        output = generator.get_qrcode()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
            temp_filename = temp_file.name
            output.save(temp_filename)
            logging.info("Temp file saved: %s", temp_filename)

        return send_file(
            temp_filename,
            as_attachment=True,
            download_name="qrcode.png",
        ), 200

    except ValueError:
        logging.error("Error generating QR code: %s", ValueError)
        return "Error generating QR code", 500

    finally:
        if 'temp_filename' in locals():
            try:
                os.remove(temp_filename)
                logging.info("Temp file removed: %s", temp_filename)

            except ValueError:
                logging.error("Error removing temp file: %s", ValueError)


@app.route('/send_email', methods=['POST'])
def send_email():
    """
    Send email based on sepcific templates
    """
    event = request.form['event']
    receiver_data = request.files['receiver']
    link = request.form['link']
    subject = request.form['subject']
    mail, passwords = request.form['email'], request.form['password']
    mail_sender = AutoMailSender(
        event,
        receiver_data,
        link,
        subject,
        mail,
        passwords
    )
    infos = mail_sender.get_data()
    mail_sender.send_mail(infos)
    logging.info("Email sent successfully")
