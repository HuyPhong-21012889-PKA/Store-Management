# order_controller.py
from database.models import Order, OrderItem, Product

class OrderController:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_order(self, customer_id, order_items):
        new_order = Order(customer_id=customer_id)
        self.db_session.add(new_order)
        self.db_session.flush()  # Lấy ID đơn hàng mới

        for item in order_items:
            product = self.db_session.query(Product).filter_by(id=item['product_id']).first()
            if product and product.quantity >= item['quantity']:
                order_detail = OrderItem(order_id=new_order.id, product_id=product.id, quantity=item['quantity'])
                product.quantity -= item['quantity']  # Cập nhật số lượng tồn kho
                self.db_session.add(order_detail)
            else:
                print(f"Insufficient stock for product '{item['product_id']}'")
        
        self.db_session.commit()
        print(f"Order created successfully for customer '{customer_id}'.")

    def update_order_status(self, order_id, status):
        order = self.db_session.query(Order).filter_by(id=order_id).first()
        if order:
            order.status = status
            self.db_session.commit()
            print(f"Order '{order_id}' status updated to '{status}'.")
        else:
            print("Order not found.")

    def cancel_order(self, order_id):
        order = self.db_session.query(Order).filter_by(id=order_id).first()
        if order:
            for detail in order.order_details:
                product = self.db_session.query(Product).filter_by(id=detail.product_id).first()
                product.quantity += detail.quantity  # Khôi phục số lượng tồn kho
            self.db_session.delete(order)
            self.db_session.commit()
            print(f"Order '{order_id}' canceled successfully.")
        else:
            print("Order not found.")
    
    def get_order(self, order_id):
        return self.db_session.query(Order).filter_by(id=order_id).first()
    
    def get_all_orders(self):
        # Lấy tất cả đơn hàng từ cơ sở dữ liệu
        return self.db_session.query(Order).all()

    def get_order_status(self, order_id):
        # Lấy tình trạng đơn hàng
        order = self.db_session.query(Order).filter(Order.id == order_id).first()
        if order:
            return order.status
        return None

    def update_order_status(self, order_id, new_status):
        # Cập nhật tình trạng đơn hàng
        order = self.db_session.query(Order).filter(Order.id == order_id).first()
        if order:
            order.status = new_status
            self.db_session.commit()  # Đảm bảo lưu thay đổi
