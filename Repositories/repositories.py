from Models.cart import Cart
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def get_cart_by_name(name):
    return Cart.query.filter_by(name=name).all()


def save_cart(cart):
    db.session.add(cart)
    db.session.commit()
    return cart.to_dict()


def save_product(product):
    db.session.add(product)
    db.session.commit()
