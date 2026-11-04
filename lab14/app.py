from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# in-memory database
items = {}

# home route
@app.route('/')
def home():
    return render_template('index.html')

# CREATE an item
@app.route('/items', methods = ["POST"])
def create_item():
    # request.get_json() method is used to read JSON data sent by the client
    data = request.get_json()

    # generate a new unique id for the new item
    item_id = str(len(items)+1)

    # add the data collected for the item
    items[item_id] = data

    return jsonify({"id" : item_id, "item": data}), 201

# READ all items
@app.route('/items', methods = ["GET"])
def get_items():
    return jsonify(items)

if __name__ == "__main__":
    app.run(debug=True)