from flask import jsonify
import requests
from Models.cart import Cart
from Models.product import Product
from Models.people import People
from Repositories.repositories import get_cart_by_name, save_cart, save_product


def save(p_id, prod_id):
    people = requests.get("http://localhost:5069/read/" + str(p_id)).json()
    product = requests.get("http://localhost:5070/read/" + str(prod_id)).json()

    people_obj = People(
        p_id=people['id'],
        name=people['name'],
        email=people['email'],
        phone=people['phone']
    )

    product_obj = Product(
        product_name=product['product_name'],
        price=product['price'],
        quantity=product['quantity']
    )
    save_product(product_obj)

    cart = Cart(
        name=people_obj.name,
        email=people_obj.email,
        products=[product_obj]
    )
    save_cart(cart)

    return cart


def list_of_items(name):
    carts = get_cart_by_name(name)
    response = {name: []}

    for cart in carts:
        cart_dict = cart.to_dict()
        response[name].append(cart_dict)

    return jsonify(response)
