# controllers/user_management_controller.py

from sqlalchemy.orm import Session
from database.models import User  # Giả sử User là model đại diện cho người dùng trong hệ thống

class UserManagementController:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_user(self, username: str, email: str, password: str) -> User:
        """Thêm người dùng mới vào hệ thống."""
        existing_user = self.db_session.query(User).filter_by(email=email).first()
        if existing_user:
            raise ValueError("Email đã được sử dụng. Vui lòng chọn email khác.")
        
        new_user = User(username=username, email=email, password=password)
        self.db_session.add(new_user)
        self.db_session.commit()
        return new_user

    def update_user(self, user_id: int, username: str = None, email: str = None, password: str = None) -> User:
        """Cập nhật thông tin người dùng."""
        user = self.db_session.query(User).get(user_id)
        if not user:
            raise ValueError("Không tìm thấy người dùng với ID này.")
        
        if username:
            user.username = username
        if email:
            if self.db_session.query(User).filter(User.email == email, User.id != user_id).first():
                raise ValueError("Email này đã được sử dụng bởi người dùng khác.")
            user.email = email
        if password:
            user.password = password

        self.db_session.commit()
        return user

    def delete_user(self, user_id: int) -> None:
        """Xóa người dùng khỏi hệ thống."""
        user = self.db_session.query(User).get(user_id)
        if not user:
            raise ValueError("Không tìm thấy người dùng với ID này.")
        
        self.db_session.delete(user)
        self.db_session.commit()

    def get_user(self, user_id: int) -> User:
        """Trả về thông tin người dùng theo ID."""
        user = self.db_session.query(User).get(user_id)
        if not user:
            raise ValueError("Không tìm thấy người dùng với ID này.")
        return user

    def list_users(self) -> list:
        """Trả về danh sách tất cả người dùng trong hệ thống."""
        return self.db_session.query(User).all()
