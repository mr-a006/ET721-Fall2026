import os
from flask import Flask, render_template, request, jsonify
import mysql.connector


app = Flask(__name__)

"""
-----------------------------
file configuration
-----------------------------
"""
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

"""
-----------------------------
MySQL Connection
-----------------------------
"""
db_config = {
    'host':'localhost',
    'user':'flaskuser',
    'password':'password123',
    'database':'image_app'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

"""
-----------------------------
LOADING PAGE ROUTE
-----------------------------
"""
@app.route('/')
def index():
    return render_template('index.html')

"""
-----------------------------
RUN APP
-----------------------------
"""
if __name__ == '__main':
    app.run(debug=True)