# helpers.py

from datetime import datetime

def format_currency(amount):
    """Chuyển đổi số thành định dạng tiền tệ."""
    return f"{amount:,.2f} VND"

def get_current_timestamp():
    """Lấy thời gian hiện tại dưới dạng chuỗi định dạng."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
