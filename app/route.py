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
    send_from_directory,
    url_for
)
from scripts.rm_bg import Remover
from scripts.heic2jpg import Converter
from scripts.make_qr import QRCodeGenerator
from scripts.email_sender_new.src.sender import AutoMailSender


app = Flask(
    __name__,
    static_url_path='/tool-box/static',
    static_folder='static',
    template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

DOWNLOAD_FOLDER = '~/Desktop' # TODO: need revise
app.jinja_loader.searchpath.append(os.path.join(os.path.dirname(__file__), 'templates'))
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

def prefix_url(url):
    if app.config.get('ENV') == "production":
        return f'/tool-box{url}'
    return url

def url_for_prefixed(endpoint, **values):
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

@app.route('/aboutus')
def about():
    """
    About page
    """
    return render_template('about.html')

@app.route('/login', methods=['GET'])
def login_page():
    """
    Serve the login page
    """
    return render_template('login.html')

@app.route('/signup', methods=['GET'])
def signup_page():
    """
    Serve the signup page
    """
    return render_template('signup.html')

@app.route('/services')
def services():
    """
    Services page
    """
    return render_template('services.html')

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

@app.route('/heic2jpg', methods=['POST'])
def heic2jpg():
    """
    Convert HEIC image to another image format
    """
    url = request.form['url']
    converter = Converter(url)
    output = converter.heic2jpg()
    temp_file = os.path.join(app.config['DOWNLOAD_FOLDER'], 'download.png')
    output.save(temp_file, "JPG", quality=95)
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
    link = request.form['link']
    subject = request.form['subject']
    mail, passwords = request.form['email'], request.form['password']
    mail_sender = AutoMailSender(event, receiver_data, link, subject, mail, passwords)
    infos = mail_sender.get_data()
    mail_sender.send_mail(infos)
    logging.info("Email sent successfully")
