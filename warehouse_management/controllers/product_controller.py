# product_controller.py
from database.models import Product

class ProductController:
    def __init__(self, db_session):
        self.db_session = db_session

    def add_product(self, name, quantity, price):
        new_product = Product(name=name, quantity=quantity, price=price)
        self.db_session.add(new_product)
        self.db_session.commit()
        print(f"Product '{name}' added successfully.")

    def update_product(self, product_id, name=None, quantity=None, price=None):
        product = self.db_session.query(Product).filter_by(id=product_id).first()
        if not product:
            print("Product not found.")
            return
        if name:
            product.name = name
        if quantity is not None:
            product.quantity = quantity
        if price is not None:
            product.price = price
        self.db_session.commit()
        print(f"Product '{product_id}' updated successfully.")

    def delete_product(self, product_id):
        product = self.db_session.query(Product).filter_by(id=product_id).first()
        if product:
            self.db_session.delete(product)
            self.db_session.commit()
            print(f"Product '{product_id}' deleted successfully.")
        else:
            print("Product not found.")
    
    def get_product(self, product_id):
        return self.db_session.query(Product).filter_by(id=product_id).first()

    def list_products(self):
        return self.db_session.query(Product).all()
