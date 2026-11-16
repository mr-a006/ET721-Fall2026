from flask import Flask, render_template, request, jsonify

import mysql.connector
app = Flask(__name__)

# ------------------------------
# Database configuration
# ------------------------------
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'todo_db'

# database connection
db = mysql.connector.connect(
    host = app.config['MYSQL_HOST'],
    user = app.config['MYSQL_USER'],
    password = app.config['MYSQL_PASSWORD'],
    database = app.config['MYSQL_DB']
)

# ------------------------------
# homepage route
# ------------------------------
@app.route('/')
def index():
    return render_template("index.html")