# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/about.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(200, 225)
        About.setMinimumSize(QtCore.QSize(200, 225))
        About.setMaximumSize(QtCore.QSize(200, 225))
        self.label_2 = QtWidgets.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(6, 110, 191, 20))
        self.label_2.setStyleSheet("text-decoration: underline;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(About)
        self.label_3.setGeometry(QtCore.QRect(6, 130, 191, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(About)
        self.label_4.setGeometry(QtCore.QRect(5, 160, 191, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.btnCloseAbout = QtWidgets.QPushButton(About)
        self.btnCloseAbout.setGeometry(QtCore.QRect(60, 190, 80, 23))
        self.btnCloseAbout.setObjectName("btnCloseAbout")
        self.lblAboutIcon = QtWidgets.QLabel(About)
        self.lblAboutIcon.setGeometry(QtCore.QRect(3, 0, 191, 111))
        self.lblAboutIcon.setText("")
        self.lblAboutIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAboutIcon.setObjectName("lblAboutIcon")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Form"))
        self.label_2.setText(_translate("About", "Version 0.1, Build 2021-01-01"))
        self.label_3.setText(_translate("About", "Written by James Bos"))
        self.label_4.setText(_translate("About", "<a href=\"#\">Source and License</a>"))
        self.btnCloseAbout.setText(_translate("About", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QWidget()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())
