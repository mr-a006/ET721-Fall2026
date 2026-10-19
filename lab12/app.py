"""
Aqeel Hussain
Oct 19, 2026
session 3: add data to a Flask app
"""

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL config
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'employee_data'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    msg = ''
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employee(name, age) VALUES (%s, %s)", (name, age))
        mysql.connection.commit()
        cur.close()

        msg = f"{name}, your data was inserted successfully"
		
    return render_template('index.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True)