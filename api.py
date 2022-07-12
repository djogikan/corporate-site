from flask import Flask, render_template
from flask_qrcode import QRcode
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
QRcode(app)
if __name__ == "__main__":
    
    app.run(debug=True, host="0.0.0.0")