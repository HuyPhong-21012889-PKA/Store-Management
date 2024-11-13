# validators.py

import re

def is_valid_email(email):
    """Kiểm tra xem chuỗi có phải là email hợp lệ không."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def is_positive_number(value):
    """Kiểm tra xem giá trị có phải là một số dương không."""
    return isinstance(value, (int, float)) and value > 0

def is_valid_product_quantity(quantity):
    """Kiểm tra xem số lượng sản phẩm có hợp lệ không (phải là số nguyên dương)."""
    return isinstance(quantity, int) and quantity > 0
