from database.models import Product, Inventory
from database.db import session

class ImportController:
    def __init__(self, db_session):
        self.db_session = db_session

    def add_import(self, product_id, quantity, import_date):
        product = self.db_session.query(Product).filter_by(id=product_id).first()
        if product:
            product.quantity += quantity
            self.db_session.commit()
            print(f"Đã cập nhật số lượng sản phẩm ID {product_id} thêm {quantity}")
        else:
            print("Sản phẩm không tồn tại")

