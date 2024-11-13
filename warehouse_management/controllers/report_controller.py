# report_controller.py
from database.models import Order, Product

class ReportController:
    def __init__(self, db_session):
        self.db_session = db_session

    def generate_sales_report(self, start_date, end_date):
        orders = self.db_session.query(Order).filter(Order.date.between(start_date, end_date)).all()
        total_sales = sum(order.total_amount() for order in orders)
        print(f"Sales Report from {start_date} to {end_date}: Total Sales = ${total_sales:.2f}")
        return total_sales
    
    def generate_inventory_report(self):
        products = self.db_session.query(Product).all()
        report = {product.name: product.quantity for product in products}
        print("Inventory Report:")
        for product_name, quantity in report.items():
            print(f"{product_name}: {quantity}")
        return report
