import sys
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication

from Final.management.libs.DataConnector import DataConnector
from Final.ui.MainWindowExt import MainWindowExt
from Final.ui.MainWindowLogin import Ui_MainWindow


class MainWindowLoginExt(QMainWindow):
    MAX_ATTEMPTS = 3  # Số lần nhập sai tối đa

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonLogin.clicked.connect(self.process_login)
        self.ui.pushButtonExit.clicked.connect(self.process_exit)

        # Khởi tạo DataConnector để đọc dữ liệu từ JSON
        self.data_connector = DataConnector("../dataset/employees.json")

        # Biến đếm số lần nhập sai
        self.login_attempts = 0

    def process_login(self):
        """Xử lý đăng nhập với danh sách nhân viên từ file JSON"""
        username = self.ui.lineEditUserName.text().strip()
        password = self.ui.lineEditUserPassword.text().strip()

        # Kiểm tra đăng nhập
        employee = self.data_connector.validate_employee_login(username, password)

        if employee:
            self.open_main_window(employee["EmployeeName"])  # Truyền tên nhân viên vào giao diện chính
        else:
            self.login_attempts += 1
            if self.login_attempts >= self.MAX_ATTEMPTS:
                self.show_exit_warning()
            else:
                self.show_login_failed_message()

    def open_main_window(self, employee_name):
        """Mở giao diện chính nếu đăng nhập thành công"""
        self.main_window = MainWindowExt(employee_name)
        self.main_window.show()
        self.close()

    def show_login_failed_message(self):
        """Hiển thị thông báo lỗi khi đăng nhập sai"""
        QMessageBox.warning(self, "Đăng nhập thất bại", f"Sai tài khoản hoặc mật khẩu!\n(Lần thử {self.login_attempts}/{self.MAX_ATTEMPTS})")

    def show_exit_warning(self):
        """Cảnh báo khi nhập sai quá nhiều lần và đóng ứng dụng"""
        QMessageBox.critical(self, "Quá số lần thử", "Bạn đã nhập sai quá 3 lần!\nChương trình sẽ tự động thoát.")
        self.close()  # Đóng cửa sổ
        sys.exit()  # Thoát hoàn toàn ứng dụng

    def process_exit(self):
        """Thoát chương trình khi bấm nút Exit"""
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowLoginExt()
    window.show()
    sys.exit(app.exec())
