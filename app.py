from flask import Flask, render_template,request
import os
from model import model_app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            filename = file.filename
            filepath = os.path.join('static/uploads', filename)  # Path to save the uploaded file
            file.save(filepath)
            # Perform any addi<LeftMouse>tional processing on the uploaded file
            label = model_app(filepath)
            return render_template('home.html', filename=filename, output = label)
    return render_template('home.html')

@app.route('/EDA', methods=['GET', 'POST'])
def plot():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            filename = file.filename
            filepath = os.path.join('static/uploads', filename)  # Path to save the uploaded file
            file.save(filepath)
            # Perform any additional processing on the uploaded file
            label = model_app(filepath)
            return render_template('home.html', filename=filename, output = label)
    return render_template('EDA.html')

