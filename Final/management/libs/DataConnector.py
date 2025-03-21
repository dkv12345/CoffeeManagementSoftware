import json
import os

from Final.management.models import Product
from Final.models.JsonFileFactory import JsonFileFactory


class DataConnector:

    def __init__(self, employee_file_path=None, manager_file_path=None):
        self.employee_file_path = employee_file_path or "/Users/dovi/ProductManagement/Final/dataset/employees.json"
        self.manager_file_path = manager_file_path or "/Users/dovi/ProductManagement/Final/dataset/managers.json"

    def _read_json_file(self, file_path):
        """Đọc dữ liệu từ file JSON, xử lý lỗi và trả về list"""
        if not file_path or not os.path.exists(file_path):
            print(f"File '{file_path}' không tồn tại!")
            return []

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except json.JSONDecodeError as e:
            print(f"Lỗi khi đọc file JSON '{file_path}': {e}")
            return []

    def read_employees(self):
        return self._read_json_file(self.employee_file_path)

    def validate_employee_login(self, username, password):
        employees = self.read_employees()
        username, password = username.strip(), password.strip()

        for emp in employees:
            stored_username = emp.get("UserName", "").strip()
            stored_password = emp.get("Password", "").strip()

            if stored_username == username and stored_password == password:
                return emp  # Trả về thông tin nhân viên

        return None

    def read_managers(self):
        managers = self._read_json_file(self.manager_file_path)

        # Chuẩn hóa dữ liệu: Xóa khoảng trắng thừa và chuyển username về chữ thường
        for manager in managers:
            manager["ManagerUsername"] = manager.get("ManagerUsername", "").strip()
            manager["ManagerPassword"] = manager.get("ManagerPassword", "").strip()

        return managers

    def validate_manager_login(self, username, password):
        """Xác thực đăng nhập quản lý"""
        managers = self.read_managers()
        username, password = username.strip().lower(), password.strip()

        for manager in managers:
            stored_username = manager.get("ManagerUsername", "").strip().lower()
            stored_password = manager.get("ManagerPassword", "").strip()

            if stored_username == username and stored_password == password:
                return manager  # Trả về thông tin quản lý

    def get_all_products(self):
        jff = JsonFileFactory()
        filename = "/Users/dovi/ProductManagement/Final/dataset/products.json"
        products = jff.read_data(filename, Product)
        return products
    def check_existing_product(self,products,id):
        for i in range(len(products)):
            product=products[i]
            if product.id==id:
                return i
        return -1

    @staticmethod
    def check_existing_customer(customers, customer_id):
        for index, customer in enumerate(customers):
            if customer.id == customer_id:
                return index
        return -1
