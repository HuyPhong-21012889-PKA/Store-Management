# controllers/supplier_management_controller.py

from sqlalchemy.orm import Session
from database.models import Supplier

class SupplierManagementController:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_supplier(self, name: str, contact_info: str, address: str) -> Supplier:
        new_supplier = Supplier(name=name, contact_info=contact_info, address=address)
        self.db_session.add(new_supplier)
        self.db_session.commit()
        return new_supplier

    def update_supplier(self, supplier_id: int, name: str = None, contact_info: str = None, address: str = None) -> Supplier:
        supplier = self.db_session.query(Supplier).get(supplier_id)
        if not supplier:
            raise ValueError("Supplier not found.")
        if name:
            supplier.name = name
        if contact_info:
            supplier.contact_info = contact_info
        if address:
            supplier.address = address
        self.db_session.commit()
        return supplier

    def delete_supplier(self, supplier_id: int) -> None:
        supplier = self.db_session.query(Supplier).get(supplier_id)
        if not supplier:
            raise ValueError("Supplier not found.")
        self.db_session.delete(supplier)
        self.db_session.commit()

    def get_supplier(self, supplier_id: int) -> Supplier:
        return self.db_session.query(Supplier).get(supplier_id)

    def list_suppliers(self) -> list:
        return self.db_session.query(Supplier).all()
