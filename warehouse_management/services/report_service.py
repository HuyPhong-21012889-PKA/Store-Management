from database.models import Order, Inventory
from database.db import session

class ReportService:
    def generate_revenue_report(self, start_date, end_date):
        orders = session.query(Order).filter(Order.date >= start_date, Order.date <= end_date).all()
        total_revenue = sum(order.total_price for order in orders)
        return {"total_revenue": total_revenue, "orders": orders}

    def generate_stock_report(self):
        stock = session.query(Inventory).all()
        stock_report = [{"product_id": item.product_id, "quantity": item.quantity} for item in stock]
        return stock_report
