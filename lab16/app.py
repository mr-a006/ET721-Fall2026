import os
import uuid
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import mysql.connector


app = Flask(__name__)

"""
-----------------------------
file configuration
-----------------------------
"""
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads')
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

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
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM images ORDER BY id DESC")
    images = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template('index.html', images=images)

"""
-----------------------------
UPLOAD IMAGE ROUTE
-----------------------------
"""
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'message': 'No image selected'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'message': 'No image selected'}), 400

    if not allowed_file(file.filename):
        return jsonify({'message': 'Invalid image format'}), 400

    filename = secure_filename(file.filename)
    unique_filename = str(uuid.uuid4()) + '_' + filename

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
    file.save(filepath)

    try:
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO images (filename) VALUES (%s)",
            (unique_filename,)
        )

        db.commit()
        cursor.close()
        db.close()

        return jsonify({
            'message': 'Image uploaded successfully!',
            'filename': unique_filename,
            'url': '/static/uploads/' + unique_filename
        }), 201

    except mysql.connector.Error as error:
        if os.path.exists(filepath):
            os.remove(filepath)

        return jsonify({'message': 'Database error: ' + str(error)}), 500

"""
-----------------------------
RUN APP
-----------------------------
"""
if __name__ == '__main__':
    app.run(debug=True)