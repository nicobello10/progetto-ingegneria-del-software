# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizzazione_liste.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from Implementazione.Gestione.GestoreUtente import GestoreUtente


class Ui_visualizzazioneliste(object):
    def setupUi(self, visualizzazioneliste):
        visualizzazioneliste.setObjectName("visualizzazioneliste")
        visualizzazioneliste.resize(735, 334)
        self.buttonBox = QtWidgets.QDialogButtonBox(visualizzazioneliste)
        self.buttonBox.setGeometry(QtCore.QRect(340, 290, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabellautenti = QtWidgets.QTableWidget(visualizzazioneliste)
        self.tabellautenti.setGeometry(QtCore.QRect(40, 10, 641, 261))
        self.tabellautenti.setObjectName("tabellautenti")
        self.tabellautenti.setColumnCount(7)
        self.tabellautenti.setRowCount(len(GestoreUtente.collectionUtenti))
        self.tabellautenti.setHorizontalHeaderLabels(["Nome","Cognome","Data di nascita","Cellulare","Username","Password","Socio"])
        self.retranslateUi(visualizzazioneliste)
        self.buttonBox.accepted.connect(visualizzazioneliste.accept) # type: ignore
        self.buttonBox.rejected.connect(visualizzazioneliste.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(visualizzazioneliste)
        for i, row in enumerate(GestoreUtente.collectionUtenti):
            item = QTableWidgetItem(GestoreUtente.collectionUtenti[i].nome)
            self.tabellautenti.setItem(i, 0, item)
            item = QTableWidgetItem(GestoreUtente.collectionUtenti[i].cognome)
            self.tabellautenti.setItem(i, 1, item)
            item = QTableWidgetItem(GestoreUtente.collectionUtenti[i].dataNascita)
            self.tabellautenti.setItem(i, 2, item)
            item = QTableWidgetItem(GestoreUtente.collectionUtenti[i].cellulare)
            self.tabellautenti.setItem(i, 3, item)
            item = QTableWidgetItem(GestoreUtente.collectionUtenti[i].nomeUtente)
            self.tabellautenti.setItem(i, 4, item)
            item = QTableWidgetItem(GestoreUtente.collectionUtenti[i].password)
            self.tabellautenti.setItem(i, 5, item)
            item = QTableWidgetItem(str(GestoreUtente.collectionUtenti[i].getTesseramento()))
            self.tabellautenti.setItem(i, 6, item)


    def retranslateUi(self, visualizzazioneliste):
        _translate = QtCore.QCoreApplication.translate
        visualizzazioneliste.setWindowTitle(_translate("visualizzazioneliste", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    visualizzazioneliste = QtWidgets.QDialog()
    ui = Ui_visualizzazioneliste()
    ui.setupUi(visualizzazioneliste)
    visualizzazioneliste.show()
    sys.exit(app.exec_())
