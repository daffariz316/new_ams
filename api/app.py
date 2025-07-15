from flask import Flask, render_template, request, redirect
import urllib.parse

app = Flask(__name__, template_folder='../templates', static_folder='../static', static_url_path='../static/assets/imgs/client')

# ===============================
# ROUTE UTAMA
# ===============================
@app.route('/')
def index():
    return render_template('index.html')

# ===============================
# ROUTE HANDLE FORM CONTACT
# ===============================
@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Nomor WhatsApp tujuan (tanpa spasi)
    whatsapp_number = '62895372499072'  # Ganti dengan nomor kamu

    # Buat pesan WhatsApp
    text = f"Halo! Saya {name} {email} {subject} {message}"

    # Encode ke URL
    encoded_text = urllib.parse.quote(text)

    # Buat URL WhatsApp API
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_text}"

    # Redirect ke WhatsApp
    return redirect(whatsapp_url)

# # ===============================
# # RUN SERVER
# # ===============================
# if __name__ == '__main__':
#     app.run(debug=True, port=5001)
