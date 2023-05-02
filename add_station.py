from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

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