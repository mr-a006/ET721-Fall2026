from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)