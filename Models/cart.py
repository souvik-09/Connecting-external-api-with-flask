from config import db


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    products = db.relationship('Product', secondary='cart_products', backref='carts')

    def to_dict(self):
        product_list = []
        for product in self.products:
            product_dict = {
                "productName": product.product_name,
                "productQuantity": product.quantity
            }
            product_list.append(product_dict)

        return {
            "name": self.name,
            "email": self.email,
            "products": product_list
        }


cart_products = db.Table(
    'cart_products',
    db.Column('cart_id', db.Integer, db.ForeignKey('cart.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('product.prod_id'))
)
