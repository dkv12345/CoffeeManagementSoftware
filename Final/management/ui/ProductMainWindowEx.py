import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from PyQt6 import QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QTableWidgetItem, QMainWindow
from Final.management.libs.DataConnector import DataConnector
from Final.management.libs.JsonFileFactory import JsonFileFactory
from Final.management.models.Product import Product
from Final.management.ui.ProductMainWindow import Ui_MainWindow
from Final.management.models.customer import Customer
import datetime

class ProductMainWindowEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dc = DataConnector()

        self.json_product_filename = "Product.json"
        self.products = self.load_products_from_json()
        self.show_products_ui()

        self.json_customer_filename = "Customer.json"
        self.customers = self.load_customers_from_json()
        self.show_customers_ui()
        self.setupDateDisplay()
        self.setupSignalAndSlot()
        self.setupDigitalClock()  # 🔹 Thêm đồng hồ
        self.date_timer = QTimer(self)

    def setupDigitalClock(self):
        """Thiết lập đồng hồ điện tử cập nhật trong textBrowser_clock."""
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateClock)
        self.timer.start(1000)  # Cập nhật mỗi giây
        self.updateClock()  # Hiển thị ngay khi mở app

    def updateClock(self):
        """Cập nhật thời gian vào textBrowser_clock."""
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.textBrowser_clock.setText(current_time)
        self.setupSignalAndSlot()

    def load_products_from_json(self):
        jff = JsonFileFactory()
        return jff.read_data(self.json_product_filename, Product)

    def save_products_to_json(self):
        jff = JsonFileFactory()
        jff.write_data(self.products, self.json_product_filename)

    def show_products_ui(self):
        self.tableWidgetProductManagement.setRowCount(0)
        for p in self.products:
            row = self.tableWidgetProductManagement.rowCount()
            self.tableWidgetProductManagement.insertRow(row)
            self.tableWidgetProductManagement.setItem(row, 0, QTableWidgetItem(str(p.id)))
            self.tableWidgetProductManagement.setItem(row, 1, QTableWidgetItem(p.name))
            self.tableWidgetProductManagement.setItem(row, 2, QTableWidgetItem(str(p.price)))
            self.tableWidgetProductManagement.setItem(row, 3, QTableWidgetItem(str(p.quantity)))

    def load_customers_from_json(self):
        jff = JsonFileFactory()
        data = jff.read_data(self.json_customer_filename, dict)
        customers = [Customer(c["id"], c["name"], c["phone"], c["customer_type"]) for c in data]
        return customers

    def save_customers_to_json(self):
        jff = JsonFileFactory()
        jff.write_data(self.customers, self.json_customer_filename)

    def show_customers_ui(self):
        self.tableWidgetCustomerManagement.setRowCount(0)
        for c in self.customers:
            row = self.tableWidgetCustomerManagement.rowCount()
            self.tableWidgetCustomerManagement.insertRow(row)
            self.tableWidgetCustomerManagement.setItem(row, 0, QTableWidgetItem(str(c.id)))
            self.tableWidgetCustomerManagement.setItem(row, 1, QTableWidgetItem(c.name))
            self.tableWidgetCustomerManagement.setItem(row, 2, QTableWidgetItem(c.phone))
            self.tableWidgetCustomerManagement.setItem(row, 3, QTableWidgetItem(c.customer_type))

    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.save_product_info)
        self.pushButtonRemove.clicked.connect(self.remove_product)
        self.pushButtonClear.clicked.connect(self.clear_product_detail)
        self.pushButtonSave_2.clicked.connect(self.search_product)
        self.tableWidgetProductManagement.itemSelectionChanged.connect(self.process_show_product_detail)

        self.pushButtonSaveCustomer.clicked.connect(self.save_customer_info)
        self.pushButtonRemoveCustomer.clicked.connect(self.remove_customer)
        self.pushButtonClearCustomer.clicked.connect(self.clear_customer_detail)
        self.pushButtonSearchCustomer.clicked.connect(self.search_customer)
        self.tableWidgetCustomerManagement.itemSelectionChanged.connect(self.process_show_customer_detail)

        self.pushButtonBarChart.clicked.connect(self.show_bar_chart)
        self.pushButtonPieChart.clicked.connect(self.show_pie_chart)
        self.pushButtonLineChart.clicked.connect(self.show_line_graph)
    def process_show_product_detail(self):
        index = self.tableWidgetProductManagement.currentRow()
        if index < 0:
            return
        product = self.products[index]
        self.lineEditProductId.setText(str(product.id))
        self.lineEditProductName.setText(product.name)
        self.lineEditPrice.setText(str(product.price))
        self.lineEditQuantity.setText(str(product.quantity))

    def clear_product_detail(self):
        self.lineEditProductId.clear()
        self.lineEditProductName.clear()
        self.lineEditPrice.clear()
        self.lineEditQuantity.clear()
        self.lineEditProductId.setFocus()

    def save_product_info(self):
        id = self.lineEditProductId.text()
        name = self.lineEditProductName.text()
        price = float(self.lineEditPrice.text())
        quantity = int(self.lineEditQuantity.text())

        p = Product(id, name, price, quantity)
        index = self.dc.check_existing_product(self.products, p.id)
        if index == -1:
            self.products.append(p)
        else:
            self.products[index] = p

        self.save_products_to_json()
        self.show_products_ui()

    def remove_product(self):
        id = self.lineEditProductId.text()
        index = self.dc.check_existing_product(self.products, id)
        if index == -1:
            return

        self.products.pop(index)
        self.save_products_to_json()
        self.show_products_ui()
        self.clear_product_detail()

    def search_product(self):
        search_id = self.lineEditProductId.text()
        for product in self.products:
            if product.id == search_id:
                self.lineEditProductName.setText(product.name)
                self.lineEditPrice.setText(str(product.price))
                self.lineEditQuantity.setText(str(product.quantity))
                return

    def process_show_customer_detail(self):
        index = self.tableWidgetCustomerManagement.currentRow()
        if index < 0:
            return
        customer = self.customers[index]
        self.lineEditCustomerId.setText(str(customer.id))
        self.lineEditCustomerName.setText(customer.name)
        self.lineEditCustomerPhone.setText(customer.phone)
        if customer.customer_type == "Normal":
            self.checkBoxNormal.setChecked(True)
            self.checkBoxVIP.setChecked(False)
        else:
            self.checkBoxNormal.setChecked(False)
            self.checkBoxVIP.setChecked(True)

    def clear_customer_detail(self):
        self.lineEditCustomerId.clear()
        self.lineEditCustomerName.clear()
        self.lineEditCustomerPhone.clear()
        self.checkBoxNormal.setChecked(False)
        self.checkBoxVIP.setChecked(False)
        self.lineEditCustomerId.setFocus()

    def save_customer_info(self):
        id = self.lineEditCustomerId.text()
        name = self.lineEditCustomerName.text()
        phone = self.lineEditCustomerPhone.text()
        customer_type = "VIP" if self.checkBoxVIP.isChecked() else "Normal"

        c = Customer(id, name, phone, customer_type)
        index = self.dc.check_existing_customer(self.customers, c.id)
        if index == -1:
            self.customers.append(c)
        else:
            self.customers[index] = c

        self.save_customers_to_json()
        self.show_customers_ui()

    def remove_customer(self):
        id = self.lineEditCustomerId.text()
        index = self.dc.check_existing_customer(self.customers, id)
        if index == -1:
            return

        self.customers.pop(index)
        self.save_customers_to_json()
        self.show_customers_ui()
        self.clear_customer_detail()

    def search_customer(self):
        search_id = self.lineEditCustomerId.text()
        for customer in self.customers:
            if customer.id == search_id:
                self.lineEditCustomerName.setText(customer.name)
                self.lineEditCustomerPhone.setText(customer.phone)
                return

    def show_pie_chart(self):
        try:
            if not self.customers:
                raise ValueError("Customer list is empty. Cannot generate pie chart.")

            plt.close('all')  # Đóng tất cả các figure đang mở
            customer_types = [c.customer_type for c in self.customers]
            type_counts = {"Normal": customer_types.count("Normal"), "VIP": customer_types.count("VIP")}

            if sum(type_counts.values()) == 0:
                raise ValueError("No customer data available for pie chart.")

            plt.figure(figsize=(6, 6))
            plt.pie(
                type_counts.values(),
                labels=type_counts.keys(),
                autopct="%1.1f%%",
                colors=["skyblue", "lightcoral"]
            )
            plt.title("Customer Type Distribution")
            plt.show()

        except ValueError as ve:
            QtWidgets.QMessageBox.warning(self, "Chart Error", str(ve))
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Chart Error", f"An error occurred: {e}")
    def show_bar_chart(self):
        try:
            if not self.products:
                raise ValueError("Product list is empty. Cannot generate bar chart.")

            plt.close('all')  # Đóng tất cả các figure đang mở
            plt.figure(figsize=(10, 6))
            product_names = [p.name for p in self.products]
            quantities = [p.quantity for p in self.products]

            sns.barplot(x=product_names, y=quantities, palette="viridis")
            plt.xlabel("Product Name")
            plt.ylabel("Quantity")
            plt.title("Product Quantity Distribution")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.show()

        except ValueError as ve:
            QtWidgets.QMessageBox.warning(self, "Chart Error", str(ve))
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Chart Error", f"An error occurred: {e}")

    def show_line_graph(self):
        try:
            file_path = "/Users/dovi/ProductManagement/Final/management/dataforchart/Revenue.csv"
            df = pd.read_csv(file_path)

            if df.empty:
                self.statusBar().showMessage("Không có dữ liệu doanh thu để hiển thị!", 3000)
                return

            plt.close('all')  # Đóng tất cả các figure đang mở
            plt.figure(figsize=(10, 5))
            product_names = df["Product Name"]
            total_revenue = df["Total Revenue"]

            plt.plot(product_names, total_revenue, marker="o", linestyle="-", color="b", linewidth=2, markersize=6)
            plt.xlabel("Product Name", fontsize=12, fontweight="bold")
            plt.ylabel("Total Revenue ($)", fontsize=12, fontweight="bold")
            plt.title("Total Revenue in 23/03/2025", fontsize=14, fontweight="bold")
            plt.xticks(rotation=20)
            plt.grid(True, linestyle="--", alpha=0.7)
            plt.show()

        except Exception as e:
            self.statusBar().showMessage(f"Lỗi khi đọc dữ liệu: {str(e)}", 3000)

    def setupDateDisplay(self):
        """Thiết lập hiển thị ngày tháng năm trong textBrowser_date."""
        self.date_timer = QTimer(self)
        self.date_timer.timeout.connect(self.updateDate)
        self.date_timer.start(1000)  # Cập nhật mỗi giây
        self.updateDate()  # Hiển thị ngay khi mở app

    def updateDate(self):
        """Cập nhật ngày tháng vào textBrowser_date."""
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        self.textBrowser_date.setText(current_date)
