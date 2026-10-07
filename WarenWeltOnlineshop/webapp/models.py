from . import db
from flask_login import UserMixin

# SQL-Alchemy-Klassen
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, index=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(50))
    company_number = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    address = db.Column(db.String(200))

    def __repr__(self):
        return f'<User {self.email}>'

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    category = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Float, nullable=False, default=0.0)
