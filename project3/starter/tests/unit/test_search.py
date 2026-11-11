import pytest
from app import create_app
from app.models import Fruit, FruitMetrics, db


@pytest.fixture(scope='module')
def test_app():
    # Setup: create a Flask app instance
    app = create_app()
    # Push an application context
    ctx = app.app_context()
    ctx.push()

    # Setup the database
    with app.app_context():
        db.create_all()

    yield app  # this is where the testing happens

    # Teardown: remove the application context
    ctx.pop()

# Add tests for the search functionality
# Start by adding some fruits to the database

# Test 1: Search by name
# Test 2: Search by variety
# Test 3: Search by season
# Test 4: Search by min quantity
# Test 5: Search by max quantity 
# Test 6: Search does not return any results

def test_searchByName_withExistingFruitName_returnsFruitsWithName(test_app):
    """
    Test the search functionality by name in the Fruit model.
    Verifies that the search method returns the correct fruits when searching by name.
    """
    # Setup - add fruits to the database
    fruits = [
        Fruit(name="Apple", quantity=10, variety="Gala", season="Winter"),
        Fruit(name="Banana", quantity=20, variety="Cavendish", season="All"),
        Fruit(name="Apple", quantity=15, variety="Fuji", season="Winter"),
    ]
    with test_app.app_context():  # Make sure you're in the db context
        db.session.bulk_save_objects(fruits)
        db.session.commit()

        # Add your test here
