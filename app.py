from flask import Flask, jsonify
from Services.services import save, list_of_items
from config import SECRET_KEY, db
from os import environ, path, getcwd
from dotenv import load_dotenv

load_dotenv(path.join(getcwd(), '.env'))


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URI')
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = SECRET_KEY
    db.init_app(app)
    print("DB Initialized Successfully")

    with app.app_context():
        @app.route('/cart/<p_id>/<prod_id>', methods=['POST'])
        def save_cart(p_id, prod_id):
            cart = save(p_id, prod_id)
            cart_dict = cart.to_dict()
            return jsonify(cart_dict)

        @app.route('/cart/<name>', methods=['GET'])
        def get_cart(name):
            items = list_of_items(name)
            return items

        # db.drop_all()
        db.create_all()
        db.session.commit()
        return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="localhost", port=5071)
