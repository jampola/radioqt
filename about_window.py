from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp, QTreeWidgetItem

from lib.ui.about import Ui_About


class AboutWindow(QtWidgets.QWidget, Ui_About):
    def __init__(self, parent=None):
        super(AboutWindow, self).__init__(parent)
        self.setupUi(self)

        self.logo = QtGui.QPixmap('/usr/share/radioqt/pixmaps/logo.png')
        self.lblAboutIcon.setPixmap(self.logo)

        self.btnCloseAbout.clicked.connect(self.close)

    def close_window(self):
        self.close()