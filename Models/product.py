from config import db


class Product(db.Model):
    prod_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

