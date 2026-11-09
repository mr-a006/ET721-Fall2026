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

    if not data or not data.get('name') or data.get('price') is None:
        return jsonify({'error': 'Invalid input'}), 400

    # generate a new unique id for the new item
    item_id = str(max([int(i) for i in items.keys()], default=0) + 1)

    # add the data collected for the item
    items[item_id] = data

    return jsonify({"id" : item_id, "item": data}), 201

# READ all items
@app.route('/items', methods = ["GET"])
def get_items():
    return jsonify(items)

# READ, UPDATE, DELETE SINGLE ITEMS
@app.route('/items/<item_id>', methods = ['GET', 'PUT', 'DELETE'])
def handle_item(item_id):
    item = items.get(item_id)

    # READ
    if request.method == "GET":
        if not item:
            return jsonify({'Error' : 'Item not found'}), 404

        return jsonify(item)

    # UPDATE
    elif request.method == "PUT":
        if not item:
            return render_template('error.html', message = "NOT FOUND", item = item), 404

        data = request.get_json()
        if not data or not data.get('name') or data.get('price') is None:
            return jsonify({'error' : 'Invalid input'}), 400

        items[item_id] = data
        return render_template('update.html', item_id = item_id, item = data)

    # DELETE
    elif request.method == "DELETE":
        if not item:
            return render_template('error.html', message = "ITEM NOT FOUND"), 404

        deleted_item = items.pop(item_id)
        return render_template('delete.html', item_id = item_id, deleted_item = deleted_item)

if __name__ == "__main__":
    app.run(debug=True)