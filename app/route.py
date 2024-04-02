import os
import logging
from flask import Flask, request, render_template, send_file
from scripts.rm_bg import Remover
from scripts.make_qr import QRCodeGenerator


app = Flask(__name__)
TEMP_FOLDER = 'temp'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    action = request.form['action']
    output = None

    if action == 'remove_background':
        image_file = request.files['image']
        remover = Remover(image_file)
        output = remover.remove_bg()
        print("Background removed")

    elif action == 'generate_qrcode':
        url = request.form['url']
        generator = QRCodeGenerator(url)
        output = generator.get_qrcode()
        print("QR code generated")

    if output:
        temp_file = os.path.join(os.getcwd(), 'download.png')
        output.save(temp_file)
        logging.info(f"Temp file saved: {temp_file}")
        return send_file(temp_file, as_attachment=True)
        