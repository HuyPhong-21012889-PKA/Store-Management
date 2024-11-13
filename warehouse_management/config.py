# config.py

import os

# Cấu hình cơ sở dữ liệu
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'user': 'your_db_user',
    'password': 'your_db_password',
    'database': 'warehouse_management'
}

# Cấu hình email SMTP
EMAIL_CONFIG = {
    'smtp_server': 'smtp.example.com',
    'smtp_port': 587,
    'email_user': 'youremail@example.com',
    'email_password': 'yourpassword'
}

DATABASE_URL = "sqlite:///warehouse_management.db"

# Các cấu hình chung khác
DEBUG = True
SECRET_KEY = os.urandom(24)
