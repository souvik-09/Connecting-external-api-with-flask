from flask import Flask, jsonify
from Services.services import save, list_of_items

app = Flask(__name__)


@app.route('/cart/<int:p_id>/<int:prod_id>', methods=['POST'])
def save_cart(p_id, prod_id):
    cart = save(p_id, prod_id)
    return jsonify(cart)


@app.route('/cart/<string:name>', methods=['GET'])
def get_cart_items(name):
    cart_items = list_of_items(name)
    return jsonify(cart_items)


if __name__ == '__main__':
    app.run()
