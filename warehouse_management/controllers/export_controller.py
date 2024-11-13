from database.models import Product
from database.db import session

class ExportController:
    def __init__(self, db_session):
        self.db_session = db_session

    def export_product(self, product_id, quantity, export_date):
        product = session.query(Product).filter_by(id=product_id).first()
        if product and product.quantity >= quantity:
            product.quantity -= quantity
            session.commit()
            print(f"Đã xuất {quantity} sản phẩm ID {product_id}")
        else:
            print("Không đủ hàng để xuất hoặc sản phẩm không tồn tại")
