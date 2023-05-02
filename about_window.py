from PyQt5 import QtWidgets, QtGui

from lib.ui.about import Ui_About


class AboutWindow(QtWidgets.QWidget, Ui_About):
    def __init__(self, parent=None):
        super(AboutWindow, self).__init__(parent)
        self.setupUi(self)

        self.logo = QtGui.QPixmap('/usr/share/radioqt/pixmaps/logo.png')
        self.lblAboutIcon.setPixmap(self.logo)
        self.lblBuild.setText("0.1")

        self.btnCloseAbout.clicked.connect(self.close)

    def close_window(self):
        self.close()