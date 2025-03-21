from PyQt6.QtWidgets import QApplication, QMainWindow

from Final.management.ui.ProductMainWindowEx import ProductMainWindowEx

app=QApplication([])
mainwindow=QMainWindow()
myui=ProductMainWindowEx()
myui.setupUi(mainwindow)
myui.show()

app.exec()