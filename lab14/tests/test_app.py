import pytest
from app import app, items

@pytest.fixture
def client():
    app.config['TESTING'] = True
    items.clear()
    with app.test_client() as client:
        yield client
    items.clear()

# ---------------------
# HOME TEST
# ---------------------
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

# ---------------------
# CREATE AN ITEM, POST METHOD
# ---------------------
def test_create_item(client):
    # create a template with id 1
    response = client.post('/items', json={'name' : 'Book', 'price' : 10})

    assert response.status_code == 201

    # test the template with id 1
    data = response.get_json()
    assert 'id' in data
    assert data['item']['name'] == 'Book'
    assert data['item']['price'] == 10

# ---------------------
# READ SINGLE ITEM
# ---------------------
def test_get_single_item(client):
    client.post('/items', json = {'name' : 'Laptop', 'price' : 900})

    response = client.get('/items/1')

    assert response.status_code == 200

    data = response.get_json()
    assert data['name'] == 'Laptop'
    assert data['price'] == 900

# ---------------------
# READ ALL ITEMS
# ---------------------
def test_get_all_items(client):
    client.post('/items', json = {'name' : 'Pen', 'price' : 1})
    client.post('/items', json = {'name' : 'Notebook', 'price' : 3})

    response = client.get('/items')

    assert response.status_code == 200
    data = response.get_json()

    assert len(data) == 2
    assert data['1']['name'] == 'Pen'
    assert data['2']['name'] == 'Notebook'
    assert data['1']['price'] == 1
    assert data['2']['price'] == 3

# ---------------------
# UPDATE ITEM
# ---------------------
def test_update_item(client):
    client.post('/items', json = {'name' : 'Phone', 'price' : 500})

    response = client.put('/items/1', json = {'name' : 'Smartphone', 'price' : 700})

    assert response.status_code == 200

    updated_response = client.get('/items/1')
    data = updated_response.get_json()

    assert data['name'] == 'Smartphone'
    assert data['price'] == 700