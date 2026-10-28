from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

import mysql.connector

app = Flask(__name__)

# database connection
def get_db_connection():
    return mysql.connector.connect(
        host = 'localhost',
        user = "flaskuser",
        password = "password123",
        database = "blogDB"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blogs')
def blogs():
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT blog.id, users.username, blog.title, blog.content, blog.created_at FROM blog JOIN users ON blog.user_id = users.userid")
            data = cursor.fetchall()
        finally:
            cursor.close()
    finally:
        connection.close()

    return render_template('blogs.html', blogs = data)

if __name__ == '__main__':
    app.run(debug=True)