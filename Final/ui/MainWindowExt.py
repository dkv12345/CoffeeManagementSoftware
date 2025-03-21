from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Final.management.ui.ManagementLoginExt import LoginWindow
from Final.models.customer import Customer
from Final.ui.MainWindow import Ui_MainWindow


class MainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self, employee_name):
        super().__init__()
        self.setupUi(self)

        self.customer_list = [
            Customer("1", "John Smith", "1234567890", "Normal"),
            Customer("2", "Emma Johnson", "0987654321", "VIP"),
            Customer("3", "Michael Brown", "1122334455", "Normal"),
            Customer("3", "Sophia Martinez", "2233445566", "VIP"),
            Customer("4", "William Anderson", "3344556677", "Normal"),
        ]

        # Khởi tạo giỏ hàng và tổng tiền
        self.cart = []
        self.total_price = 0
        self.current_customer = None  # Lưu khách hàng hiện tại
        self.pushButtonNextBill.clicked.connect(self.clear_bill)

        # Hiển thị tên nhân viên lên giao diện
        self.staffname.setText(f"Staff: {employee_name}")

        # Kết nối sự kiện cho các nút
        self.sortcoffeebeans.clicked.connect(self.sort_1)
        self.sortcoldbrew.clicked.connect(self.sort_2)
        self.sortmatcha.clicked.connect(self.sort_3)
        self.sortchocolate.clicked.connect(self.sort_4)
        self.reload.clicked.connect(self.full)
        self.pushButtonPM.clicked.connect(self.openmanagementlogin)
        self.pushButton_loadCusType.clicked.connect(self.display_customer_info)
        self.pushButton_TB.clicked.connect(self.calculate_total)  # Thêm nút tính tổng hóa đơn

        # Kết nối nút mua hàng
        self.setup_cart_buttons()

    def openmanagementlogin(self):
        self.close()  # Đóng cửa sổ chính
        self.main_window = LoginWindow()
        self.main_window.show()

    def display_customer_info(self):
        """Hiển thị thông tin khách hàng khi nhập số điện thoại"""
        phone_number = self.lineEdit_PhoneNum.text().strip()
        self.current_customer = None  # Reset khách hàng hiện tại

        for customer in self.customer_list:
            if customer.phone == phone_number:
                self.current_customer = customer
                self.lineEdit_CustomerType.setText(f"{customer.name} - {customer.customer_type}")
                return

        QMessageBox.warning(self, "Lỗi", "Không tìm thấy khách hàng!")
        self.lineEdit_CustomerType.clear()

    def setup_cart_buttons(self):
        """Gán sự kiện click cho các nút thêm sản phẩm vào giỏ hàng"""
        self.buychocolatebalance.clicked.connect(lambda: self.add_to_cart("Chocolate Balance", 36))
        self.buydarkchocolate.clicked.connect(lambda: self.add_to_cart("Dark Chocolate", 50))
        self.buymilkchocolate.clicked.connect(lambda: self.add_to_cart("Milk Chocolate", 55))
        self.buyclassicalroast.clicked.connect(lambda: self.add_to_cart("Medium Roast Blend", 45))
        self.buyvanillacoldbrew.clicked.connect(lambda: self.add_to_cart("Vanilla Cold Brew", 40))
        self.buymediumroast.clicked.connect(lambda: self.add_to_cart("Classical Cold Brew", 38))
        self.buyvanillaroast.clicked.connect(lambda: self.add_to_cart("Vanilla Roast", 40))
        self.buyujimatcha.clicked.connect(lambda: self.add_to_cart("Uji Matcha", 70))
        self.buykyotomatcha.clicked.connect(lambda: self.add_to_cart("Kyoto Matcha", 80))
        self.buyspecialblend.clicked.connect(lambda: self.add_to_cart("Special Blend", 35))
        self.buydarkroast.clicked.connect(lambda: self.add_to_cart("Dark Roast", 45))
        self.buylightroast.clicked.connect(lambda: self.add_to_cart("Light Roast", 35))
        self.buymochacoffee.clicked.connect(lambda: self.add_to_cart("Mocha Coffee", 30))
        self.buyinstantcoffee.clicked.connect(lambda: self.add_to_cart("Instant Coffee", 30))

    def add_to_cart(self, item_name, price):
        """Thêm sản phẩm vào giỏ hàng"""
        for index, (name, item_price, quantity) in enumerate(self.cart):
            if name == item_name:
                self.cart[index] = (name, item_price, quantity + 1)
                self.update_cart_display()
                return

        self.cart.append((item_name, price, 1))
        self.update_cart_display()

    def update_cart_display(self):
        """Cập nhật hiển thị giỏ hàng"""
        self.tableWidget.setRowCount(0)
        for item_name, price, quantity in self.cart:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(item_name))
            self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(quantity)))
            self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(f"${price * quantity}"))

    def calculate_total(self):
        """Tính tổng hóa đơn và áp dụng giảm giá nếu khách hàng là VIP"""
        self.total_price = sum(price * quantity for _, price, quantity in self.cart)

        if self.current_customer and self.current_customer.customer_type == "VIP":
            discount = self.total_price * 0.2
            final_price = self.total_price - discount
            self.labelTB.setText(f"(VIP 20% Off): ${final_price:.2f}")
        else:
            self.labelTB.setText(f"{self.total_price:.2f}")

    def full(self):
        """Hiển thị tất cả sản phẩm"""
        self.set_visibility(all_visible=True)

    def sort_1(self):
        """Hiển thị sản phẩm Coffee Beans"""
        self.set_visibility(coffee=True)

    def sort_2(self):
        """Hiển thị sản phẩm Cold Brew"""
        self.set_visibility(coldbrew=True)

    def sort_3(self):
        """Hiển thị sản phẩm Matcha"""
        self.set_visibility(matcha=True)

    def sort_4(self):
        """Hiển thị sản phẩm Chocolate"""
        self.set_visibility(chocolate=True)

    def set_visibility(self, coffee=False, coldbrew=False, matcha=False, chocolate=False, all_visible=False):
        """Cập nhật trạng thái hiển thị sản phẩm"""
        visible_states = {
            "coffee": coffee or all_visible,
            "coldbrew": coldbrew or all_visible,
            "matcha": matcha or all_visible,
            "chocolate": chocolate or all_visible,
        }

        self.imagecoffee.setVisible(visible_states["coffee"])
        self.imagecoffee_2.setVisible(visible_states["coffee"])
        self.imagecoffee_3.setVisible(visible_states["coffee"])
        self.imagecoffee_4.setVisible(visible_states["coffee"])
        self.imagecoffee_5.setVisible(visible_states["coffee"])
        self.imagecoffee_6.setVisible(visible_states["coffee"])
        self.imagecoffee_7.setVisible(visible_states["coffee"])

        self.imagecoldbrew.setVisible(visible_states["coldbrew"])
        self.imagecoldbrew_2.setVisible(visible_states["coldbrew"])

        self.imagematcha.setVisible(visible_states["matcha"])
        self.imagematcha_2.setVisible(visible_states["matcha"])

        self.imagechocolate.setVisible(visible_states["chocolate"])
        self.imagechocolate_2.setVisible(visible_states["chocolate"])
        self.imagechocolate_3.setVisible(visible_states["chocolate"])

    def clear_bill(self):
        """Xoá toàn bộ sản phẩm trong bảng hoá đơn"""
        self.tableWidget.setRowCount(0)  # Xoá toàn bộ dòng trong bảng
        self.cart.clear()  # Xoá danh sách giỏ hàng
        self.total_price = 0  # Reset tổng tiền
        self.labelTB.setText("")  # Cập nhật lại tổng hoá đơn trên giao diện
        self.lineEdit_PhoneNum.setText("")  # Cập nhật lại tổng hoá đơn trên giao diện
        self.lineEdit_CustomerType.setText("")  # Cập nhật lại tổng hoá đơn trên giao diện
