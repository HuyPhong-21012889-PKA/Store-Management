# inventory_controller.py
from database.models import Product

class InventoryController:
    def __init__(self, db_session):
        self.db_session = db_session

    def check_inventory(self, product_id):
        product = self.db_session.query(Product).filter_by(id=product_id).first()
        if product:
            print(f"Product '{product_id}' has {product.quantity} items in stock.")
            return product.quantity
        else:
            print("Product not found.")
            return None
    
    def update_inventory(self, product_id, quantity):
        product = self.db_session.query(Product).filter_by(id=product_id).first()
        if product:
            product.quantity = quantity
            self.db_session.commit()
            print(f"Inventory updated for product '{product_id}' with new quantity: {quantity}.")
        else:
            print("Product not found.")
    def get_inventory_report(self):
        # Truy vấn để lấy thông tin báo cáo thống kê kho
        report_data = []

        # Truy vấn tất cả các sản phẩm trong kho
        products = self.db_session.query(Product).all()

        for product in products:
            # Lấy tổng số lượng nhập vào từ bảng nhập hàng
            total_imported = self.db_session.query(Import).filter(Import.product_id == product.id).with_entities(func.sum(Import.quantity)).scalar() or 0
            
            # Lấy tổng số lượng xuất ra từ bảng xuất hàng
            total_exported = self.db_session.query(Export).filter(Export.product_id == product.id).with_entities(func.sum(Export.quantity)).scalar() or 0

            # Số lượng tồn kho hiện tại
            current_stock = total_imported - total_exported

            # Lưu thông tin vào báo cáo
            report_data.append({
                'product_id': product.id,
                'product_name': product.name,
                'total_imported': total_imported,
                'total_exported': total_exported,
                'current_stock': current_stock
            })

        return report_data