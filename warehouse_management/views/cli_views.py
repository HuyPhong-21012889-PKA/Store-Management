from controllers.import_controller import ImportController
from controllers.export_controller import ExportController
from controllers.user_management_controller import UserManagementController
from controllers.inventory_controller import InventoryController
from controllers.order_controller import OrderController
from controllers.revenue_report_controller import RevenueReportController
from database.db import session

# Khởi tạo các controller với db_session
import_controller = ImportController(db_session=session)
export_controller = ExportController(db_session=session)
user_controller = UserManagementController(db_session=session)
inventory_controller = InventoryController(db_session=session)
order_controller = OrderController(db_session=session)
report_controller = RevenueReportController(db_session=session)

def run_cli():
    print("Chào mừng bạn đến với hệ thống quản lý kho hàng CLI!")
    while True:
        print("\nLựa chọn chức năng:")
        print("1. Nhập hàng")
        print("2. Xuất hàng")
        print("3. Quản lý người dùng")
        print("4. Kiểm tra tồn kho")
        print("5. Quản lý đơn hàng")
        print("6. Báo cáo doanh thu")
        print("7. Thoát")

        choice = input("Chọn chức năng (1-7): ")
        
        if choice == '1':
            manage_imports()
        elif choice == '2':
            manage_exports()
        elif choice == '3':
            manage_users()
        elif choice == '4':
            check_inventory()
        elif choice == '5':
            manage_orders()
        elif choice == '6':
            generate_revenue_report()
        elif choice == '7':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

def manage_imports():
    """Giao diện CLI cho nhập hàng."""
    product_id = int(input("Nhập ID sản phẩm: "))
    quantity = int(input("Nhập số lượng nhập: "))
    import_date = input("Nhập ngày nhập (YYYY-MM-DD): ")
    import_controller.add_import(product_id, quantity, import_date)
    print(f"Đã nhập {quantity} cho sản phẩm ID {product_id}.")

def manage_exports():
    """Giao diện CLI cho xuất hàng."""
    product_id = int(input("Nhập ID sản phẩm: "))
    quantity = int(input("Nhập số lượng xuất: "))
    export_date = input("Nhập ngày xuất (YYYY-MM-DD): ")
    export_controller.process_export(product_id, quantity, export_date)
    print(f"Đã xuất {quantity} sản phẩm ID {product_id}.")

def manage_users():
    """Giao diện CLI cho quản lý người dùng."""
    while True:
        print("\nQuản lý người dùng:")
        print("1. Thêm người dùng")
        print("2. Cập nhật người dùng")
        print("3. Xóa người dùng")
        print("4. Xem danh sách người dùng")
        print("5. Quay lại")

        choice = input("Chọn chức năng (1-5): ")

        if choice == '1':
            username = input("Nhập tên người dùng: ")
            email = input("Nhập email người dùng: ")
            password = input("Nhập mật khẩu: ")
            user = user_controller.add_user(username, email, password)
            print(f"Người dùng '{user.username}' đã được thêm.")

        elif choice == '2':
            user_id = int(input("Nhập ID người dùng cần cập nhật: "))
            username = input("Nhập tên mới (để trống nếu không đổi): ")
            email = input("Nhập email mới (để trống nếu không đổi): ")
            password = input("Nhập mật khẩu mới (để trống nếu không đổi): ")
            user = user_controller.update_user(user_id, username, email, password)
            print(f"Người dùng '{user.username}' đã được cập nhật.")

        elif choice == '3':
            user_id = int(input("Nhập ID người dùng cần xóa: "))
            user_controller.delete_user(user_id)
            print("Người dùng đã được xóa.")

        elif choice == '4':
            users = user_controller.list_users()
            print("\nDanh sách người dùng:")
            for user in users:
                print(f"ID: {user.id}, Tên: {user.username}, Email: {user.email}")

        elif choice == '5':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

def check_inventory():
    """Giao diện CLI cho kiểm tra tồn kho."""
    inventory = inventory_controller.get_all_inventory()
    print("\nDanh sách tồn kho:")
    for item in inventory:
        print(f"ID sản phẩm: {item.id}, Tên: {item.name}, Số lượng tồn: {item.quantity}")

def manage_orders():
    """Giao diện CLI cho quản lý đơn hàng."""
    while True:
        print("\nQuản lý đơn hàng:")
        print("1. Thêm đơn hàng")
        print("2. Cập nhật đơn hàng")
        print("3. Xóa đơn hàng")
        print("4. Xem danh sách đơn hàng")
        print("5. Quay lại")

        choice = input("Chọn chức năng (1-5): ")

        if choice == '1':
            customer_name = input("Nhập tên khách hàng: ")
            product_id = int(input("Nhập ID sản phẩm: "))
            quantity = int(input("Nhập số lượng: "))
            order = order_controller.create_order(customer_name, product_id, quantity)
            print(f"Đơn hàng cho khách hàng '{order.customer_name}' đã được tạo.")

        elif choice == '2':
            order_id = int(input("Nhập ID đơn hàng cần cập nhật: "))
            customer_name = input("Nhập tên khách hàng mới (để trống nếu không đổi): ")
            quantity = input("Nhập số lượng mới (để trống nếu không đổi): ")
            quantity = int(quantity) if quantity else None
            order = order_controller.update_order(order_id, customer_name, quantity)
            print(f"Đơn hàng ID {order.id} đã được cập nhật.")

        elif choice == '3':
            order_id = int(input("Nhập ID đơn hàng cần xóa: "))
            order_controller.delete_order(order_id)
            print("Đơn hàng đã được xóa.")

        elif choice == '4':
            orders = order_controller.list_orders()
            print("\nDanh sách đơn hàng:")
            for order in orders:
                print(f"ID: {order.id}, Khách hàng: {order.customer_name}, Số lượng: {order.quantity}")

        elif choice == '5':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

def generate_revenue_report():
    """Giao diện CLI cho báo cáo doanh thu."""
    report = report_controller.generate_revenue_report()
    print("\nBáo cáo doanh thu:")
    for item in report:
        print(f"Ngày: {item['date']}, Doanh thu: {item['revenue']}")

