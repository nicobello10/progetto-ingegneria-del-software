# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registrazione_socio.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from Implementazione.Gestione.GestoreUtenti import GestoreUtenti
from Implementazione.Viste.confermatesseramento import Ui_confermatesseramento
from Implementazione.Viste.erroretesseramento import Ui_erroretesseramento

class Ui_registrazionesocio(object):
    def tesseramento(self):
        cont = 0
        tipoTesseramento = ""
        appoggioCF = self.codicefiscale.text()
        appoggioEM = self.email.text()
        flag1 = 0
        flag2 = 0
        for x in appoggioEM:
            if(x=="@"):
                flag1=1
            if(x=="."):
                flag2 = 1

        if (len(appoggioCF)>=16 and flag1 ==1 and flag2== 1 ):
            codiceFiscale=self.codicefiscale.text()
            email = self.email.text()
            if self.tennis.isChecked():
                tipoTesseramento = "Tennis"
            elif self.paddle.isChecked():
                tipoTesseramento = "Paddle"
            elif self.tennis_paddle.isChecked():
                tipoTesseramento = "Tennis + Paddle"
            self.popup()
            GestoreUtenti.creaTesseramento(email, codiceFiscale, tipoTesseramento)
        else :
            self.popupET()





    def popup(self):
        self.window_tesseramento = QtWidgets.QDialog()
        self.ui_tesseramento = Ui_confermatesseramento()
        self.ui_tesseramento.setupUi(self.window_tesseramento)
        self.window_tesseramento.show()


    def popupET(self):
        self.window_etesseramento = QtWidgets.QDialog()
        self.ui_etesseramento = Ui_erroretesseramento()
        self.ui_etesseramento.setupUi(self.window_etesseramento)
        self.window_etesseramento.show()


    def setupUi(self, registrazionesocio):
        registrazionesocio.setObjectName("registrazionesocio")
        registrazionesocio.resize(400, 300)
        self.codicefiscale = QtWidgets.QLineEdit(registrazionesocio)
        self.codicefiscale.setGeometry(QtCore.QRect(172, 30, 141, 21))
        self.codicefiscale.setObjectName("codicefiscale")
        self.label = QtWidgets.QLabel(registrazionesocio)
        self.label.setGeometry(QtCore.QRect(69, 30, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(registrazionesocio)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 41, 20))
        self.label_2.setObjectName("label_2")
        self.email = QtWidgets.QLineEdit(registrazionesocio)
        self.email.setGeometry(QtCore.QRect(173, 60, 141, 21))
        self.email.setObjectName("email")
        self.tennis = QtWidgets.QRadioButton(registrazionesocio)
        self.tennis.setGeometry(QtCore.QRect(210, 100, 100, 20))
        self.tennis.setObjectName("tennis")
        self.paddle = QtWidgets.QRadioButton(registrazionesocio)
        self.paddle.setGeometry(QtCore.QRect(210, 120, 100, 20))
        self.paddle.setObjectName("paddle")
        self.tennis_paddle = QtWidgets.QRadioButton(registrazionesocio)
        self.tennis_paddle.setGeometry(QtCore.QRect(210, 140, 121, 20))
        self.tennis_paddle.setObjectName("tennis_paddle")
        self.frame = QtWidgets.QFrame(registrazionesocio)
        self.frame.setGeometry(QtCore.QRect(70, 90, 261, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 91, 51))
        self.label_3.setObjectName("label_3")
        self.invia = QtWidgets.QPushButton(registrazionesocio)
        self.invia.setGeometry(QtCore.QRect(230, 230, 113, 32))
        self.invia.setObjectName("Invia")
        self.frame.raise_()
        self.codicefiscale.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.email.raise_()
        self.tennis.raise_()
        self.paddle.raise_()
        self.tennis_paddle.raise_()
        self.invia.raise_()

        #azioni dei pulsanti
        if (GestoreUtenti.utenteConnesso.getTesseramento() ==True
                or GestoreUtenti.utenteConnesso.isAdmin == True
                or GestoreUtenti.utenteConnesso.isCustode== True):
            self.invia.setEnabled(False)
        else:
            self.invia.clicked.connect(self.tesseramento)

        self.retranslateUi(registrazionesocio)
        QtCore.QMetaObject.connectSlotsByName(registrazionesocio)

    def retranslateUi(self, registrazionesocio):
        _translate = QtCore.QCoreApplication.translate
        registrazionesocio.setWindowTitle(_translate("registrazionesocio", "Form"))
        self.label.setText(_translate("registrazionesocio", "Codice Fiscale"))
        self.label_2.setText(_translate("registrazionesocio", "E-mail"))
        self.tennis.setText(_translate("registrazionesocio", "Tennis"))
        self.paddle.setText(_translate("registrazionesocio", "Paddle"))
        self.tennis_paddle.setText(_translate("registrazionesocio", "Tennis + Paddle"))
        self.label_3.setText(_translate("registrazionesocio", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Tipo di </span></p><p align=\"center\"><span style=\" font-weight:600;\">tesseramento</span></p></body></html>"))
        self.invia.setText(_translate("registrazionesocio", "Invia"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registrazionesocio = QtWidgets.QWidget()
    ui = Ui_registrazionesocio()
    ui.setupUi(registrazionesocio)
    registrazionesocio.show()
    sys.exit(app.exec_())
