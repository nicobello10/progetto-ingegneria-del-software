from PyQt5.QtWidgets import QApplication,QWidget
from Viste.home import Ui_Form


app=QApplication([])
window=QWidget()
home=Ui_Form()
home.setupUi(window)
window.show()
app.exec()