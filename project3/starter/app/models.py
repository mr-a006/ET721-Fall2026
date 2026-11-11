from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Fruit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    variety = db.Column(db.String(80))
    season = db.Column(db.String(80))

    # The `validates` decorator from SQLAlchemy is used for validation logic
    # When creating or modifying Fruit instance, it will automatically be called
    # and will raise an AssertionError if it cannot validate
    @validates('name')
    def validate_name(self, key, name):
        assert name, 'Name is required'
        assert len(name) > 2, 'Name must be more than 2 characters'
        return name

    @validates('quantity')
    def validate_quantity(self, key, quantity):
        assert isinstance(quantity, int), 'Quantity must be an integer'
        assert quantity >= 0, 'Quantity must be non-negative'
        return quantity

    @staticmethod
    def search(name=None, variety=None, season=None, min_quantity=None, max_quantity=None):
        query = Fruit.query
        if name:
            query = query.filter(Fruit.name.ilike(f'%{name}%'))
        if variety:
            query = query.filter(Fruit.variety.ilike(f'%{variety}%'))
        if season:
            query = query.filter(Fruit.season.ilike(f'%{season}%'))
        if min_quantity is not None:
            query = query.filter(Fruit.quantity >= min_quantity)
        if max_quantity is not None:
            query = query.filter(Fruit.quantity <= max_quantity)
        return query.all()

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'variety': self.variety,
            'season': self.season
        }

class FruitMetrics:
    @staticmethod
    def total_fruits(fruits):
        return len(fruits)

    @staticmethod
    def average_quantity(fruits):
        if not fruits:
            return 0
        return sum(fruit.quantity for fruit in fruits) / len(fruits)

    @staticmethod
    def most_common_fruit(fruits):
        if not fruits:
            return None
        fruit_counts = {}
        for fruit in fruits:
            fruit_counts[fruit.name] = fruit_counts.get(fruit.name, 0) + 1
        return max(fruit_counts, key=fruit_counts.get)
