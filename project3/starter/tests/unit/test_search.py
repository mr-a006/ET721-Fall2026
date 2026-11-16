import pytest
from app import create_app
from app.models import Fruit, FruitMetrics, db


@pytest.fixture
def test_app():
    # Setup: create a Flask app instance
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})

    with app.app_context():
        db.create_all()

        # Add initial fruits to the database
        fruits = [
            Fruit(name="Apple", quantity=10, variety="Gala", season="Winter"),
            Fruit(name="Banana", quantity=20, variety="Cavendish", season="All"),
            Fruit(name="Apple", quantity=15, variety="Fuji", season="Winter"),
        ]

        db.session.add_all(fruits)
        db.session.commit()

        yield app

        db.session.remove()
        db.drop_all()


# Test 1: Search by name
def test_searchByName_withExistingFruitName_returnsFruitsWithName(test_app):
    """
    Test the search functionality by name in the Fruit model.
    Verifies that the search method returns the correct fruits when searching by name.
    """
    with test_app.app_context():
        results = Fruit.search(name="Apple")

        assert len(results) == 2
        assert all(fruit.name == "Apple" for fruit in results)


# Test 2: Search by variety
def test_searchByVariety_withExistingVariety_returnsFruitsWithVariety(test_app):
    with test_app.app_context():
        results = Fruit.search(variety="Gala")

        assert len(results) == 1
        assert results[0].variety == "Gala"


# Test 3: Search by season
def test_searchBySeason_withExistingSeason_returnsFruitsWithSeason(test_app):
    with test_app.app_context():
        results = Fruit.search(season="Winter")

        assert len(results) == 2
        assert all(fruit.season == "Winter" for fruit in results)


# Test 4: Search by minimum quantity
def test_searchByMinQuantity_withExistingQuantity_returnsMatchingFruits(test_app):
    with test_app.app_context():
        results = Fruit.search(min_quantity=15)

        assert len(results) == 2
        assert all(fruit.quantity >= 15 for fruit in results)


# Test 5: Search by maximum quantity
def test_searchByMaxQuantity_withExistingQuantity_returnsMatchingFruits(test_app):
    with test_app.app_context():
        results = Fruit.search(max_quantity=15)

        assert len(results) == 2
        assert all(fruit.quantity <= 15 for fruit in results)


# Test 6: Search does not return any results
def test_search_withNoMatchingResults_returnsEmptyList(test_app):
    with test_app.app_context():
        results = Fruit.search(name="Pineapple")

        assert results == []