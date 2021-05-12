from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp, QTreeWidgetItem

from lib.ui.addstation import Ui_StationForm

class AddStationWindow(QtWidgets.QWidget, Ui_StationForm):
    station_signal = pyqtSignal(list)
    def __init__(self, parent=None):
        super(AddStationWindow, self).__init__(parent)
        self.setupUi(self)

        self.btnAdd.clicked.connect(self.add_station)
        self.btnClose.clicked.connect(self.close)

    def add_station(self):
        self.station_signal.emit([self.txtStationName.text(),self.txtStationUrl.text()])
        self.txtStationName.setText("")
        self.txtStationUrl.setText("")

    def edit_station(self,data):
        self.txtStationName.setText(data[0])
        self.txtStationUrl.setText(data[1])