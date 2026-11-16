import pytest
from app import create_app
from app.models import Fruit, FruitMetrics, db


def test_createFruit_withValidData_createsFruitWithCorrectAttributes():
    """
    Test the creation of a Fruit instance with valid parameters.
    Verifies that the name and quantity of the fruit are set correctly.
    """
    fruit = Fruit(name="Apple", quantity=10)
    assert fruit.name == "Apple"
    assert fruit.quantity == 10

def test_calculateTotalFruits_withFruitsList_returnsCorrectFruitCount():
    """
    Test the calculation of the total number of fruits in an inventory.
    Checks if the total_fruits method returns the correct count.
    """
    fruits = [Fruit(name="Apple", quantity=10), Fruit(name="Banana", quantity=5)]
    assert FruitMetrics.total_fruits(fruits) == 2

def test_calculateAverageQuantity_withFruitsList_returnsCorrectAverage():
    """
    Test the calculation of the average quantity of fruits in an inventory.
    Checks if the average_quantity method computes the correct average.
    """
    fruits = [Fruit(name="Apple", quantity=10), Fruit(name="Banana", quantity=5)]
    assert FruitMetrics.average_quantity(fruits) == 7.5

def test_identifyMostCommonFruit_withFruitsList_returnsMostFrequentFruit():
    """
    Test to identify the most common fruit in an inventory.
    Checks if the most_common_fruit method correctly identifies the fruit that appears most frequently.
    """
    fruits = [Fruit(name="Apple", quantity=10), Fruit(name="Apple", quantity=5), Fruit(name="Banana", quantity=8)]
    assert FruitMetrics.most_common_fruit(fruits) == "Apple"

def test_createFruit_withValidDetails_createsFruitSuccessfully():
    """
    Test the creation of a valid Fruit instance.
    Verifies that a fruit with valid name and quantity is created without errors.
    """
    valid_fruit = Fruit(name="Apple", quantity=10)
    assert valid_fruit.name == "Apple"
    assert valid_fruit.quantity == 10

def test_createFruit_withInvalidName_raisesAssertionError():
    """
    Test the creation of a Fruit instance with an invalid name.
    Verifies that an AssertionError is raised when the name is empty.
    """
    with pytest.raises(AssertionError):
        invalid_fruit = Fruit(name="", quantity=10)

def test_createFruit_withNegativeQuantity_raisesAssertionError():
    """
    Test the creation of a Fruit instance with an invalid quantity.
    Verifies that an AssertionError is raised when the quantity is negative.
    """
    with pytest.raises(AssertionError):
        invalid_fruit = Fruit(name="Apple", quantity=-5)

def test_createFruit_withNonIntegerQuantity_raisesAssertionError():
    """
    Test the creation of a Fruit instance with an invalid quantity type.
    Verifies that an AssertionError is raised when the quantity is not an integer.
    """
    with pytest.raises(AssertionError):
        invalid_fruit = Fruit(name="Apple", quantity="ten")

def test_calculateAverageQuantity_withEmptyList_returnsZero():
    """
    Test the average quantity calculation with an empty inventory.
    Verifies that zero is returned when there are no fruits.
    """
    assert FruitMetrics.average_quantity([]) == 0


def test_identifyMostCommonFruit_withEmptyList_returnsNone():
    """
    Test identifying the most common fruit with an empty inventory.
    Verifies that None is returned when there are no fruits.
    """
    assert FruitMetrics.most_common_fruit([]) is None


def test_serializeFruit_withValidFruit_returnsCorrectDictionary():
    """
    Test the serialization of a Fruit instance.
    Verifies that all fruit attributes are returned in a dictionary.
    """
    fruit = Fruit(name="Apple", quantity=10, variety="Gala", season="Winter")
    result = fruit.serialize()

    assert result['name'] == "Apple"
    assert result['quantity'] == 10
    assert result['variety'] == "Gala"
    assert result['season'] == "Winter"

def test_isExpired_withPastExpirationDate_returnsTrue():
    from datetime import date, timedelta

    fruit = Fruit(name="Apple", quantity=10)
    fruit.expiration_date = date.today() - timedelta(days=1)

    assert fruit.is_expired() is True


def test_isExpired_withFutureExpirationDate_returnsFalse():
    from datetime import date, timedelta

    fruit = Fruit(name="Apple", quantity=10)
    fruit.expiration_date = date.today() + timedelta(days=5)

    assert fruit.is_expired() is False