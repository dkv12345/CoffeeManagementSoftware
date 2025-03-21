import sys
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication

from Final.management.libs.DataConnector import DataConnector
from Final.management.ui.ManagementLogin import Ui_MainWindow
from Final.management.ui.ProductMainWindowEx import ProductMainWindowEx


class LoginWindow(QMainWindow):
    """Giao diện đăng nhập dành cho Manager"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối sự kiện nút bấm
        self.ui.pushButtonLogin.clicked.connect(self.process_login)
        self.ui.pushButtonExit.clicked.connect(self.process_exit)

        # Khởi tạo DataConnector để đọc dữ liệu Manager từ JSON
        self.data_connector = DataConnector(
            manager_file_path="/Users/dovi/ProductManagement/Final/dataset/managers.json")

        # Biến đếm số lần đăng nhập sai
        self.failed_attempts = 0
        self.max_attempts = 3  # Giới hạn số lần nhập sai

    def process_login(self):
        username = self.ui.lineEdit_ManagerUsername.text().strip().lower()
        password = self.ui.lineEdit_ManagerPassword.text().strip()

        manager = self.data_connector.validate_manager_login(username, password)

        if manager:
            self.open_main_window()
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= self.max_attempts:
                QMessageBox.critical(self, "Đăng nhập thất bại", "Bạn đã nhập sai quá 3 lần. Chương trình sẽ thoát.")
                sys.exit()
            else:
                self.show_login_failed_message()

    def open_main_window(self):
        self.product_window = ProductMainWindowEx()
        self.product_window.show()
        self.close()

    def show_login_failed_message(self):
        """Hiển thị thông báo lỗi khi đăng nhập thất bại"""
        QMessageBox.warning(self, "Đăng nhập thất bại",
                            f"Tên đăng nhập hoặc mật khẩu không đúng! ({self.failed_attempts}/{self.max_attempts} lần)")

    def process_exit(self):
        """Thoát chương trình khi bấm nút Exit"""
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
