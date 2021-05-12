# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/addstation.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StationForm(object):
    def setupUi(self, StationForm):
        StationForm.setObjectName("StationForm")
        StationForm.resize(400, 100)
        StationForm.setMinimumSize(QtCore.QSize(400, 100))
        StationForm.setMaximumSize(QtCore.QSize(400, 100))
        self.txtStationName = QtWidgets.QLineEdit(StationForm)
        self.txtStationName.setGeometry(QtCore.QRect(90, 10, 301, 26))
        self.txtStationName.setObjectName("txtStationName")
        self.txtStationUrl = QtWidgets.QLineEdit(StationForm)
        self.txtStationUrl.setGeometry(QtCore.QRect(90, 40, 301, 26))
        self.txtStationUrl.setObjectName("txtStationUrl")
        self.btnAdd = QtWidgets.QPushButton(StationForm)
        self.btnAdd.setGeometry(QtCore.QRect(90, 70, 83, 26))
        self.btnAdd.setObjectName("btnAdd")
        self.btnClose = QtWidgets.QPushButton(StationForm)
        self.btnClose.setGeometry(QtCore.QRect(308, 70, 83, 26))
        self.btnClose.setObjectName("btnClose")
        self.label = QtWidgets.QLabel(StationForm)
        self.label.setGeometry(QtCore.QRect(3, 13, 81, 20))
        self.label.setStyleSheet("text-decoration: underline;")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(StationForm)
        self.label_2.setGeometry(QtCore.QRect(3, 43, 81, 20))
        self.label_2.setStyleSheet("text-decoration: underline;")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(StationForm)
        QtCore.QMetaObject.connectSlotsByName(StationForm)

    def retranslateUi(self, StationForm):
        _translate = QtCore.QCoreApplication.translate
        StationForm.setWindowTitle(_translate("StationForm", "Form"))
        self.txtStationName.setPlaceholderText(_translate("StationForm", "Station Name"))
        self.txtStationUrl.setPlaceholderText(_translate("StationForm", "Stream URL"))
        self.btnAdd.setText(_translate("StationForm", "Save"))
        self.btnClose.setText(_translate("StationForm", "Close"))
        self.label.setText(_translate("StationForm", "Name"))
        self.label_2.setText(_translate("StationForm", "Stream URL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StationForm = QtWidgets.QWidget()
    ui = Ui_StationForm()
    ui.setupUi(StationForm)
    StationForm.show()
    sys.exit(app.exec_())
