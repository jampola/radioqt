from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp, QTreeWidgetItem
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot

from lib.ui.searchwindow import Ui_Form

from icecast_stream_list import get_stream_list

class SearchWindow(QtWidgets.QWidget, Ui_Form):
    station_signal = pyqtSignal(list)
    def __init__(self, parent=None):
        super(SearchWindow, self).__init__(parent)
        self.setupUi(self)

        self.btnCloseSearch.clicked.connect(self.close)
        self.btnSearch.clicked.connect(self.station_search)
        self.btnAddStation.clicked.connect(self.add_station_to_favourites)
    def close_window(self):
        self.close()

    def add_station_to_favourites(self):
        self.station_signal.emit([self.treeStationSearchResult.currentItem().text(0),self.treeStationSearchResult.currentItem().text(1)])

        return

    def station_search(self):
        search_text = self.txtSearch.text()
        results = get_stream_list(search_text)
        if results:
            self.treeStationSearchResult.clear()
            for url in results:
                QTreeWidgetItem(self.treeStationSearchResult,[url['name'],url['url_resolved']])
        # else notify the user that no results were found
        return