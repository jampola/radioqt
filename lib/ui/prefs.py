# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/prefs.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Prefs(object):
    def setupUi(self, Prefs):
        Prefs.setObjectName("Prefs")
        Prefs.resize(250, 315)
        Prefs.setMinimumSize(QtCore.QSize(250, 315))
        Prefs.setMaximumSize(QtCore.QSize(250, 315))
        self.groupBox = QtWidgets.QGroupBox(Prefs)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 231, 261))
        self.groupBox.setObjectName("groupBox")
        self.optBoolTooltips = QtWidgets.QCheckBox(self.groupBox)
        self.optBoolTooltips.setGeometry(QtCore.QRect(10, 50, 201, 24))
        self.optBoolTooltips.setObjectName("optBoolTooltips")
        self.optBoolMinimized = QtWidgets.QCheckBox(self.groupBox)
        self.optBoolMinimized.setGeometry(QtCore.QRect(10, 70, 201, 24))
        self.optBoolMinimized.setObjectName("optBoolMinimized")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 191, 18))
        self.label.setStyleSheet("font-weight: bold;")
        self.label.setObjectName("label")
        self.leStationsJSON = QtWidgets.QLineEdit(self.groupBox)
        self.leStationsJSON.setGeometry(QtCore.QRect(10, 140, 201, 26))
        self.leStationsJSON.setText("")
        self.leStationsJSON.setObjectName("leStationsJSON")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 201, 18))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 191, 18))
        self.label_6.setStyleSheet("font-weight: bold;")
        self.label_6.setObjectName("label_6")
        self.leFavsJSON = QtWidgets.QLineEdit(self.groupBox)
        self.leFavsJSON.setGeometry(QtCore.QRect(10, 190, 201, 26))
        self.leFavsJSON.setText("")
        self.leFavsJSON.setObjectName("leFavsJSON")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 170, 201, 18))
        self.label_7.setObjectName("label_7")
        self.btnClose = QtWidgets.QPushButton(Prefs)
        self.btnClose.setGeometry(QtCore.QRect(10, 280, 231, 26))
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(Prefs)
        QtCore.QMetaObject.connectSlotsByName(Prefs)

    def retranslateUi(self, Prefs):
        _translate = QtCore.QCoreApplication.translate
        Prefs.setWindowTitle(_translate("Prefs", "Dialog"))
        self.groupBox.setTitle(_translate("Prefs", "Preferences"))
        self.optBoolTooltips.setText(_translate("Prefs", "Show song in tooltip"))
        self.optBoolMinimized.setText(_translate("Prefs", "Start minimized"))
        self.label.setText(_translate("Prefs", "General"))
        self.leStationsJSON.setPlaceholderText(_translate("Prefs", "/home/james/.stations.json"))
        self.label_5.setText(_translate("Prefs", "Stations JSON"))
        self.label_6.setText(_translate("Prefs", "Paths"))
        self.leFavsJSON.setPlaceholderText(_translate("Prefs", "/home/james/.radiofavs.json"))
        self.label_7.setText(_translate("Prefs", "Favourites JSON"))
        self.btnClose.setText(_translate("Prefs", "Save and Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Prefs = QtWidgets.QDialog()
    ui = Ui_Prefs()
    ui.setupUi(Prefs)
    Prefs.show()
    sys.exit(app.exec_())
