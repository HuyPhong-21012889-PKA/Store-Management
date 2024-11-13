from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URL  # Đảm bảo bạn có cấu hình DATABASE_URL trong config.py

# Tạo đối tượng Base cho các lớp ORM
Base = declarative_base()

# Thiết lập kết nối cơ sở dữ liệu
engine = create_engine(DATABASE_URL)

# Thiết lập session
Session = scoped_session(sessionmaker(bind=engine))

# Định nghĩa session để sử dụng trong toàn bộ ứng dụng
session = Session()

# Hàm khởi tạo cơ sở dữ liệu (tạo bảng nếu chưa tồn tại)
def init_db():
    import database.models  # Import các mô hình ORM để SQLAlchemy biết cấu trúc bảng
    Base.metadata.create_all(bind=engine)

# Hàm đóng session khi không cần thiết nữa
def close_session():
    session.remove()
