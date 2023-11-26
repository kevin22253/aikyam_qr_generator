from flask import Flask, render_template, request, jsonify
import qrcode
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json
    name = data['name']
    cc_code = data['ccCode']
    college = data['college']

    # Generate QR code
    qr_data = f"Name: {name}\nCC Code: {cc_code}\nCollege: {college}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code image
    qr_image_path = f'static/{name}_invitation_pass.png'
    img.save(qr_image_path)

    return jsonify({'qrImagePath': qr_image_path})

if __name__ == '__main__':
    app.run(debug=True)
