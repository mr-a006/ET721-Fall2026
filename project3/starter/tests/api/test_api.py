import json
import pytest
from datetime import date, timedelta
from app import create_app
from app.models import db, Fruit

@pytest.fixture
def app():
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
    with app.app_context():
        db.create_all()
        # Put some initial data into the database
        fruits = [
            Fruit(name="Apple", quantity=10, variety="Gala", season="Winter"),
            Fruit(name="Banana", quantity=20, variety="Cavendish", season="All"),
        ]
        db.session.bulk_save_objects(fruits)
        db.session.commit()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_getAllFruits_whenDatabaseHasFruits_returnsFruitsList(client):
    """
    Test fetching all fruits from the database
    Validates that the GET request to '/api/fruits' returns a 200 status code,
    the correct number of fruits, and specific data of the fruits
    """
    response = client.get('/api/fruits')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data) == 2  # Adjust based on your initial data
    assert data[0]['name'] == 'Apple'

def test_addFruit_withValidData_returnsSuccessMessageAndFruitId(client):
    """
    Test adding a new fruit to the database
    Validates that the POST request to '/api/fruits' adds the fruit correctly,
    and returns a 201 status code along with a success message and the fruit's ID
    """
    new_fruit = {"name": "Orange", "quantity": 5, "variety": "Navel", "season": "Winter"}
    response = client.post('/api/fruits', json=new_fruit)
    data = json.loads(response.data)
    assert response.status_code == 201
    assert data['message'] == 'Fruit added successfully'
    assert 'id' in data

def test_home_returnsWelcomeMessage(client):
    response = client.get('/')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert 'message' in data


def test_updateFruit_withExistingFruit_updatesFruitSuccessfully(client):
    updated_fruit = {"name": "Green Apple", "quantity": 25}
    response = client.put('/api/fruits/1', json=updated_fruit)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Fruit updated successfully'


def test_updateFruit_withNonExistingFruit_returnsNotFound(client):
    response = client.put('/api/fruits/999', json={"name": "Orange"})
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['message'] == 'Fruit not found'


def test_deleteFruit_withExistingFruit_deletesFruitSuccessfully(client):
    response = client.delete('/api/fruits/1')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Fruit deleted successfully'


def test_deleteFruit_withNonExistingFruit_returnsNotFound(client):
    response = client.delete('/api/fruits/999')
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['message'] == 'Fruit not found'


def test_searchFruits_withMatchingName_returnsMatchingFruits(client):
    response = client.get('/api/fruits/search?name=Apple')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['name'] == 'Apple'


def test_searchFruits_withNoMatchingResults_returnsMessage(client):
    response = client.get('/api/fruits/search?name=Pineapple')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'No fruits found matching the search criteria'

def test_addFruit_withExpirationDate_savesExpirationDate(client):
    expiration = (date.today() - timedelta(days=1)).isoformat()
    new_fruit = {"name": "Orange", "quantity": 5, "variety": "Navel", "season": "Winter", "expiration_date": expiration}
    response = client.post('/api/fruits', json=new_fruit)
    data = json.loads(response.data)

    assert response.status_code == 201
    assert data['message'] == 'Fruit added successfully'

    fruits = client.get('/api/fruits').get_json()
    orange = next(fruit for fruit in fruits if fruit['name'] == 'Orange')

    assert orange['expiration_date'] == expiration

def test_getExpiredFruits_returnsOnlyExpiredFruits(client):
    expired_date = (date.today() - timedelta(days=1)).isoformat()
    future_date = (date.today() + timedelta(days=5)).isoformat()

    expired_fruit = {"name": "Mango", "quantity": 5, "variety": "Alphonso", "season": "Summer", "expiration_date": expired_date}
    fresh_fruit = {"name": "Peach", "quantity": 8, "variety": "Yellow", "season": "Summer", "expiration_date": future_date}

    client.post('/api/fruits', json=expired_fruit)
    client.post('/api/fruits', json=fresh_fruit)

    response = client.get('/api/fruits/expired')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['name'] == 'Mango'

def test_getExpiredFruits_whenNoFruitsHaveExpired_returnsEmptyList(client):
    response = client.get('/api/fruits/expired')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data == []