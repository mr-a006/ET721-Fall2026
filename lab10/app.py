"""
Aqeel Hussain
Oct 13, 2026
lab 10: intro to Flask
"""
from flask import Flask, render_template, redirect, url_for

"""
create an object named 'app' from the Flask module.
"""

app = Flask(__name__)

# set the routing to the main page (loading page)
# 'route' decorator is used to access the root URL

@app.route('/')
def index():
    name = "Aqeel Hussain"
    fruits = ['apple', 'kiwis', 'oranges']
    return render_template("index.html", username = name, listfruits = fruits)

@app.route('/about')
def about():
    return '<h1>About Us</h1>'

@app.route('/quotes')
def quotes():
    # return '<h1> Quotes</h1>'
    return redirect(url_for('index'))


# set the 'app' to run if you execute the file directly (not when it is imported)
# __name__ set to __main__ if the script is running directly from the main file
if __name__ == '__main__':
    app.run(debug=True)