import tkinter as tk
from tkinter import ttk
import datetime
from tkinter import messagebox, simpledialog
from controllers.user_management_controller import UserManagementController
from controllers.import_controller import ImportController
from controllers.export_controller import ExportController
from controllers.inventory_controller import InventoryController
from controllers.order_controller import OrderController
from controllers.supplier_management_controller import SupplierManagementController
from database.db import session

# Khởi tạo các controller
user_management_controller = UserManagementController(db_session=session)
supplier_controller = SupplierManagementController(db_session=session)
import_controller = ImportController(db_session=session)
export_controller = ExportController(db_session=session)
inventory_controller = InventoryController(db_session=session)
order_controller = OrderController(db_session=session)

# Tạo ứng dụng chính
class WarehouseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Warehouse Management System")
        self.root.geometry("600x450")  # Kích thước cửa sổ lớn hơn
        self.root.configure(bg="#f4f4f4")  # Màu nền sáng

        # Tạo menu
        self.create_main_menu()

    def create_main_menu(self):

        frame = ttk.Frame(self.root, padding="20")
        frame.grid(row=0, column=0, sticky="nsew")

        label = ttk.Label(frame, text="Warehouse Management System", font=("Arial", 18, "bold"))
        label.grid(row=0, column=0, columnspan=2, pady=20)

        # Các nút bấm chính
        user_button = ttk.Button(frame, text="Quản lí người dùng", width=20, command=self.handle_user_management)
        user_button.grid(row=1, column=0, pady=10)  # Adjust row position as needed
        
        supplier_button = ttk.Button(frame, text="Quản lý Nhà Cung Cấp", width=20, command=self.handle_supplier_management)
        supplier_button.grid(row=2, column=0, pady=10)

        import_button = ttk.Button(frame, text="Nhập hàng", width=20, command=self.handle_import)
        import_button.grid(row=3, column=0, pady=10)

        export_button = ttk.Button(frame, text="Xuất hàng", width=20, command=self.handle_export)
        export_button.grid(row=4, column=0, pady=10)

        inventory_button = ttk.Button(frame, text="Kiểm tra tồn kho", width=20, command=self.handle_inventory_check)
        inventory_button.grid(row=5, column=0, pady=10)

        order_button = ttk.Button(frame, text="Tạo hóa đơn", width=20, command=self.handel_order)
        order_button.grid(row=6, column=0, pady=10)

        order_management_button = ttk.Button(frame, text="Quản lí đơn hàng", width=20, command=self.handle_order_management)  
        order_management_button.grid(row=7, column=0, pady=10)

        order_update_button = ttk.Button(frame, text="Cập nhật đơn hàng", width=20, command=self.handle_update_order_status)
        order_update_button.grid(row=8, column=0, pady=10)

        report_button = ttk.Button(frame, text="Báo cáo thống kê kho", width=20, command=self.handle_report)
        report_button.grid(row=9, column=0, pady=10)

    def handle_user_management(self):
        self.clear_window()
        label = ttk.Label(self.root, text="Quản lí người dùng", font=("Arial", 14))
        label.grid(row=0, column=0, pady=20)

        # Add buttons for user actions
        add_user_button = ttk.Button(self.root, text="Thêm người dùng", command=self.add_user)
        add_user_button.grid(row=1, column=0, pady=5, sticky="ew")

        update_user_button = ttk.Button(self.root, text="Cập nhật người dùng", command=self.update_user)
        update_user_button.grid(row=2, column=0, pady=5, sticky="ew")

        delete_user_button = ttk.Button(self.root, text="Xóa người dùng", command=self.delete_user)
        delete_user_button.grid(row=3, column=0, pady=5, sticky="ew")

        # Nút quay lại
        back_button = ttk.Button(self.root, text="Quay lại", width=20, command=self.create_main_menu)
        back_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Add Treeview for displaying users
        tree = ttk.Treeview(self.root, columns=("User ID", "Username", "Email"), show="headings")
        tree.grid(row=5, column=0, padx=10, pady=20)

        # Set up columns
        tree.heading("User ID", text="ID Người Dùng")
        tree.heading("Username", text="Tên Người Dùng")
        tree.heading("Email", text="Email")

        # Fetch users and insert into tree
        users = user_management_controller.list_users()
        for user in users:
            tree.insert("", "end", values=(user.id, user.username, user.email))

    def add_user(self):
        username = simpledialog.askstring("Thêm người dùng", "Tên người dùng:")
        email = simpledialog.askstring("Thêm người dùng", "Email:")
        password = simpledialog.askstring("Thêm người dùng", "Mật khẩu:")
        try:
            user_management_controller.add_user(username, email, password)
            messagebox.showinfo("Success", "Người dùng đã được thêm.")
            self.handle_user_management()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_user(self):
        user_id = simpledialog.askinteger("Cập nhật người dùng", "ID người dùng:")
        username = simpledialog.askstring("Cập nhật người dùng", "Tên người dùng mới:")
        email = simpledialog.askstring("Cập nhật người dùng", "Email mới:")
        password = simpledialog.askstring("Cập nhật người dùng", "Mật khẩu mới:")
        try:
            user_management_controller.update_user(user_id, username, email, password)
            messagebox.showinfo("Success", "Người dùng đã được cập nhật.")
            self.handle_user_management()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_user(self):
        user_id = simpledialog.askinteger("Xóa người dùng", "ID người dùng:")
        try:
            user_management_controller.delete_user(user_id)
            messagebox.showinfo("Success", "Người dùng đã được xóa.")
            self.handle_user_management()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def handle_supplier_management(self):
        self.clear_window()
        label = ttk.Label(self.root, text="Quản lý Nhà Cung Cấp", font=("Arial", 14))
        label.grid(row=0, column=0, pady=20, padx=10, sticky="w")

        # Tạo frame chứa thông tin nhập liệu
        form_frame = ttk.Frame(self.root, padding="10")
        form_frame.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

        # Nhập liệu thông tin nhà cung cấp
        ttk.Label(form_frame, text="ID Nhà Cung Cấp:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        id_entry = ttk.Entry(form_frame, width=25)
        id_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(form_frame, text="Tên Nhà Cung Cấp:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        name_entry = ttk.Entry(form_frame, width=25)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(form_frame, text="Thông Tin Liên Hệ:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        contact_entry = ttk.Entry(form_frame, width=25)
        contact_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(form_frame, text="Địa Chỉ:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        address_entry = ttk.Entry(form_frame, width=25)
        address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Hàm thêm nhà cung cấp
        def add_supplier():
            name = name_entry.get()
            contact_info = contact_entry.get()
            address = address_entry.get()
            try:
                supplier_controller.add_supplier(name, contact_info, address)
                messagebox.showinfo("Success", "Nhà cung cấp đã được thêm!")
                self.handle_supplier_management()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        # Hàm cập nhật nhà cung cấp
        def update_supplier():
            try:
                supplier_id = int(id_entry.get())
                name = name_entry.get()
                contact_info = contact_entry.get()
                address = address_entry.get()
                supplier_controller.update_supplier(supplier_id, name, contact_info, address)
                messagebox.showinfo("Success", "Thông tin nhà cung cấp đã được cập nhật!")
                self.handle_supplier_management()
            except ValueError as e:
                messagebox.showerror("Error", "Vui lòng nhập ID hợp lệ.")

        # Hàm xóa nhà cung cấp
        def delete_supplier():
            try:
                supplier_id = int(id_entry.get())
                supplier_controller.delete_supplier(supplier_id)
                messagebox.showinfo("Success", "Nhà cung cấp đã được xóa!")
                self.handle_supplier_management()
            except ValueError as e:
                messagebox.showerror("Error", "Vui lòng nhập ID hợp lệ.")

        # Tạo các nút bấm Thêm, Cập nhật, Xóa
        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.grid(row=2, column=0, pady=10, padx=10, sticky="ew")

        add_button = ttk.Button(button_frame, text="Thêm", width=20, command=add_supplier)
        add_button.grid(row=0, column=0, padx=10, pady=5)

        update_button = ttk.Button(button_frame, text="Cập Nhật", width=20, command=update_supplier)
        update_button.grid(row=0, column=1, padx=10, pady=5)

        delete_button = ttk.Button(button_frame, text="Xóa", width=20, command=delete_supplier)
        delete_button.grid(row=0, column=2, padx=10, pady=5)

        # Treeview để hiển thị danh sách nhà cung cấp
        tree_frame = ttk.Frame(self.root, padding="10")
        tree_frame.grid(row=3, column=0, pady=10, padx=10, sticky="ew")

        tree = ttk.Treeview(tree_frame, columns=("ID", "Tên Nhà Cung Cấp", "Thông Tin Liên Hệ", "Địa Chỉ"), show="headings")
        tree.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tree.heading("ID", text="ID")
        tree.heading("Tên Nhà Cung Cấp", text="Tên Nhà Cung Cấp")
        tree.heading("Thông Tin Liên Hệ", text="Thông Tin Liên Hệ")
        tree.heading("Địa Chỉ", text="Địa Chỉ")

        # Lấy dữ liệu nhà cung cấp từ controller và hiển thị lên Treeview
        suppliers = supplier_controller.list_suppliers()
        for supplier in suppliers:
            tree.insert("", "end", values=(supplier.id, supplier.name, supplier.contact_info, supplier.address))

        # Nút quay lại
        back_button = ttk.Button(self.root, text="Quay lại", width=20, command=self.create_main_menu)
        back_button.grid(row=4, column=0, pady=10, padx=10)


    def handle_import(self):
        self.clear_window()
        label = ttk.Label(self.root, text="Nhập hàng", font=("Arial", 14))
        label.grid(row=0, column=0, pady=20)

        ttk.Label(self.root, text="ID Sản phẩm:").grid(row=1, column=0, padx=10, pady=5)
        product_id_entry = ttk.Entry(self.root, width=25)
        product_id_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Số lượng:").grid(row=2, column=0, padx=10, pady=5)
        quantity_entry = ttk.Entry(self.root, width=25)
        quantity_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Ngày nhập (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
        import_date_entry = ttk.Entry(self.root, width=25)
        import_date_entry.grid(row=3, column=1, padx=10, pady=5)

        def submit_import():
            product_id = int(product_id_entry.get())
            quantity = int(quantity_entry.get())
            import_date = import_date_entry.get()
            import_controller.add_import(product_id, quantity, import_date)
            messagebox.showinfo("Success", f"Đã cập nhật số lượng sản phẩm ID {product_id} thêm {quantity}")
            self.create_main_menu()

        submit_button = ttk.Button(self.root, text="Xác nhận", width=20, command=submit_import)
        submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        back_button = ttk.Button(self.root, text="Quay lại", width=20, command=self.create_main_menu)
        back_button.grid(row=5, column=0, columnspan=2, pady=10)

    def handle_export(self):
        self.clear_window()
        label = ttk.Label(self.root, text="Xuất hàng", font=("Arial", 14))
        label.grid(row=0, column=0, pady=20)

        ttk.Label(self.root, text="ID Sản phẩm:").grid(row=1, column=0, padx=10, pady=5)
        product_id_entry = ttk.Entry(self.root, width=25)
        product_id_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Số lượng:").grid(row=2, column=0, padx=10, pady=5)
        quantity_entry = ttk.Entry(self.root, width=25)
        quantity_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Ngày xuất (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
        export_date_entry = ttk.Entry(self.root, width=25)
        export_date_entry.grid(row=3, column=1, padx=10, pady=5)

        def submit_export():
            product_id = int(product_id_entry.get())
            quantity = int(quantity_entry.get())
            export_date = export_date_entry.get()
            export_controller.process_export(product_id, quantity, export_date)
            messagebox.showinfo("Success", f"Đã xuất số lượng sản phẩm ID {product_id} là {quantity}")
            self.create_main_menu()

        submit_button = ttk.Button(self.root, text="Xác nhận", width=20, command=submit_export)
        submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        back_button = ttk.Button(self.root, text="Quay lại", width=20, command=self.create_main_menu)
        back_button.grid(row=5, column=0, columnspan=2, pady=10)

    def handle_inventory_check(self):
        self.clear_window()
        label = ttk.Label(self.root, text="Kiểm tra tồn kho", font=("Arial", 14))
        label.grid(row=0, column=0, pady=20)

        # Hiển thị thông tin tồn kho
        back_button = ttk.Button(self.root, text="Quay lại", width=20, command=self.create_main_menu)
        back_button.grid(row=5, column=0, pady=10)

    def handle_report(self):
        self.clear_window()
        label = ttk.Label(self.root, text="Báo Cáo Thống Kê Kho", font=("Arial", 14))
        label.grid(row=0, column=0, pady=20)

        # Tạo Treeview để hiển thị báo cáo
        tree = ttk.Treeview(self.root, columns=("Product ID", "Product Name", "Total Imported", "Total Exported", "Current Stock"), show="headings")
        tree.grid(row=1, column=0, padx=10, pady=20)

        # Định dạng cột
        tree.heading("Product ID", text="ID Sản Phẩm")
        tree.heading("Product Name", text="Tên Sản Phẩm")
        tree.heading("Total Imported", text="Tổng Nhập")
        tree.heading("Total Exported", text="Tổng Xuất")
        tree.heading("Current Stock", text="Tồn Kho")

        # Lấy dữ liệu báo cáo từ controller
        report_data = inventory_controller.get_inventory_report()
        for row in report_data:
            tree.insert("", "end", values=(row["product_id"], row["product_name"], row["total_imported"], row["total_exported"], row["current_stock"]))

        back_button = ttk.Button(self.root, text="Quay lại", width=20, command=self.create_main_menu)
        back_button.grid(row=2, column=0, pady=10)
        
    def handel_order(self):
        self.clear_window()
        label = ttk.Label(self.root, text="Tạo hóa đơn", font=("Arial", 14))
        label.grid(row=0, column=0, pady=20)

        ttk.Label(self.root, text="Tên khách hàng:").grid(row=1, column=0, padx=10, pady=5)
        customer_name_entry = ttk.Entry(self.root, width=25)
        customer_name_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="ID Sản phẩm:").grid(row=2, column=0, padx=10, pady=5)
        product_id_entry = ttk.Entry(self.root, width=25)
        product_id_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Số lượng:").grid(row=3, column=0, padx=10, pady=5)
        quantity_entry = ttk.Entry(self.root, width=25)
        quantity_entry.grid(row=3, column=1, padx=10, pady=5)

        def submit_order():
            customer_name = customer_name_entry.get()
            product_id = int(product_id_entry.get())
            quantity = int(quantity_entry.get())
            order_controller.create_order(customer_name, product_id, quantity)
            messagebox.showinfo("Success", "Đơn hàng đã được tạo thành công!")
            self.create_main_menu()

        submit_button = ttk.Button(self.root, text="Xác nhận", width=20, command=submit_order)
        submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        back_button = ttk.Button(self.root, text="Quay lại", width=20, command=self.create_main_menu)
        back_button.grid(row=5, column=0, columnspan=2, pady=10)

    def handle_order_management(self):
        self.clear_window()
        label = ttk.Label(self.root, text="Quản lý đơn hàng", font=("Arial", 14))
        label.grid(row=0, column=0, pady=20)

        # Tạo một Treeview để hiển thị các đơn hàng
        tree = ttk.Treeview(self.root, columns=("Order ID", "Customer Name", "Product ID", "Quantity", "Status"), show="headings")
        tree.grid(row=1, column=0, padx=10, pady=20)

        # Định dạng cột
        tree.heading("Order ID", text="ID Đơn Hàng")
        tree.heading("Customer Name", text="Tên Khách Hàng")
        tree.heading("Product ID", text="ID Sản Phẩm")
        tree.heading("Quantity", text="Số Lượng")
        tree.heading("Status", text="Tình Trạng")

        # Lấy dữ liệu đơn hàng từ controller
        orders = order_controller.get_all_orders()
        for order in orders:
            tree.insert("", "end", values=(order.id, order.customer_name, order.product_id, order.quantity, order.status))

        # Nút Quay lại
        back_button = ttk.Button(self.root, text="Quay lại", width=20, command=self.create_main_menu)
        back_button.grid(row=5, column=0, columnspan=2, pady=10)
    
    def handle_update_order_status(self):
        self.clear_window()
        label = ttk.Label(self.root, text="Cập nhật tình trạng đơn hàng", font=("Arial", 14))
        label.grid(row=0, column=0, pady=20)

        # Nhập ID đơn hàng và tình trạng mới
        ttk.Label(self.root, text="ID Đơn Hàng:").grid(row=1, column=0, padx=10, pady=5)
        order_id_entry = ttk.Entry(self.root, width=25)
        order_id_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Tình trạng mới:").grid(row=2, column=0, padx=10, pady=5)
        status_entry = ttk.Entry(self.root, width=25)
        status_entry.grid(row=2, column=1, padx=10, pady=5)

        def submit_update_status():
            order_id = int(order_id_entry.get())
            new_status = status_entry.get()

            # Cập nhật tình trạng đơn hàng
            order_controller.update_order_status(order_id, new_status)
            messagebox.showinfo("Success", f"Tình trạng đơn hàng ID {order_id} đã được cập nhật thành {new_status}")
            self.create_main_menu()

        submit_button = ttk.Button(self.root, text="Xác nhận", width=20, command=submit_update_status)
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)

        back_button = ttk.Button(self.root, text="Quay lại", width=20, command=self.create_main_menu)
        back_button.grid(row=4, column=0, columnspan=2, pady=10)


    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.grid_forget()


def run_gui():
    root = tk.Tk()
    app = WarehouseApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
