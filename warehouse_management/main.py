# main.py

from views.cli_views import run_cli
from views.gui_views import run_gui
from config import EMAIL_CONFIG, DEBUG
from services.notification_service import NotificationService
from database.db import init_db, session

# Import controllers
from controllers.import_controller import ImportController
from controllers.export_controller import ExportController
from controllers.inventory_controller import InventoryController
from controllers.order_controller import OrderController
from controllers.revenue_report_controller import RevenueReportController
from controllers.user_management_controller import UserManagementController
from controllers.stock_report_controller import StockReportController

def initialize_services():
    notification_service = NotificationService(
        smtp_server=EMAIL_CONFIG['smtp_server'],
        smtp_port=EMAIL_CONFIG['smtp_port'],
        email_user=EMAIL_CONFIG['email_user'],
        email_password=EMAIL_CONFIG['email_password']
    )
    return notification_service

def main():
    print("Khởi động hệ thống quản lý hàng hóa...")
    init_db()

    # Khởi tạo các controller với session
    import_controller = ImportController(db_session=session)
    export_controller = ExportController(db_session=session)
    inventory_controller = InventoryController(db_session=session)
    order_controller = OrderController(db_session=session)
    revenue_report_controller = RevenueReportController(db_session=session)
    user_management_controller = UserManagementController(db_session=session)
    stock_report_controller = StockReportController(db_session=session)

    # Khởi tạo các dịch vụ cần thiết
    notification_service = initialize_services()

    # Khởi chạy giao diện GUI và truyền các controller vào
    run_gui()

if __name__ == "__main__":
    main()
