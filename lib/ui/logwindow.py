# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/logwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 225)
        Form.setMinimumSize(QtCore.QSize(400, 225))
        Form.setMaximumSize(QtCore.QSize(400, 225))
        self.twSongLog = QtWidgets.QTreeWidget(Form)
        self.twSongLog.setGeometry(QtCore.QRect(10, 10, 381, 181))
        self.twSongLog.setStyleSheet("font-size: 15px;\n"
"")
        self.twSongLog.setIndentation(0)
        self.twSongLog.setHeaderHidden(True)
        self.twSongLog.setObjectName("twSongLog")
        self.btnFindYouTube = QtWidgets.QPushButton(Form)
        self.btnFindYouTube.setGeometry(QtCore.QRect(10, 198, 121, 22))
        self.btnFindYouTube.setObjectName("btnFindYouTube")
        self.btnCloseFavorites = QtWidgets.QPushButton(Form)
        self.btnCloseFavorites.setGeometry(QtCore.QRect(311, 197, 80, 23))
        self.btnCloseFavorites.setObjectName("btnCloseFavorites")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.twSongLog.headerItem().setText(0, _translate("Form", "Date Time"))
        self.twSongLog.headerItem().setText(1, _translate("Form", "Title"))
        self.btnFindYouTube.setText(_translate("Form", "Find on YouTube"))
        self.btnCloseFavorites.setText(_translate("Form", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
