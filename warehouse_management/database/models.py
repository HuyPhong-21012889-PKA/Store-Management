from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base
from datetime import datetime

# Mô hình cho bảng sản phẩm
class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Quan hệ với bảng OrderItem
    order_items = relationship("OrderItem", back_populates="product")


# Mô hình cho bảng đơn hàng
class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String, nullable=False)
    customer_email = Column(String)
    total_amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Quan hệ với bảng OrderItem
    order_items = relationship("OrderItem", back_populates="order")


# Mô hình cho bảng OrderItem (chi tiết đơn hàng)
class OrderItem(Base):
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    # Quan hệ với Order và Product
    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")


# Mô hình cho bảng tồn kho
class Inventory(Base):
    __tablename__ = 'inventory'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    stock_level = Column(Integer, nullable=False)
    last_updated = Column(DateTime, default=datetime.utcnow)

    # Quan hệ với bảng Product
    product = relationship("Product")


# Mô hình cho bảng người dùng (nhân viên quản lý)
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
    address = Column(String, nullable=True)

    def __repr__(self):
        return f"<Supplier(name={self.name}, contact_info={self.contact_info}, address={self.address})>"

# Mô hình cho bảng báo cáo doanh thu
class RevenueReport(Base):
    __tablename__ = 'revenue_reports'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    generated_at = Column(DateTime, default=datetime.utcnow)
    total_revenue = Column(Float, nullable=False)
    number_of_orders = Column(Integer, nullable=False)


# Mô hình cho bảng báo cáo tồn kho
class InventoryReport(Base):
    __tablename__ = 'inventory_reports'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    generated_at = Column(DateTime, default=datetime.utcnow)
    total_items = Column(Integer, nullable=False)
    low_stock_items = Column(Integer, nullable=False)
