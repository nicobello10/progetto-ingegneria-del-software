from PyQt5.QtWidgets import QApplication, QMainWindow
from menu import Ui_MainWindow



app = QApplication([])
window = QMainWindow()
menu = Ui_MainWindow()
menu.setupUi(window)
window.show()
app.exec()
