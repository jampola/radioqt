from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtCore import pyqtSignal

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
        self.comboSearchOption.currentTextChanged.connect(self.update_search_placeholder)
        self.btnClearSearch.clicked.connect(self.clear_search)

    def clear_search(self):
        self.treeStationSearchResult.clear()

    def update_search_placeholder(self):
        self.txtSearch.setPlaceholderText(f"Search by {self.comboSearchOption.currentText()}")

    def close_window(self):
        self.close()

    def add_station_to_favourites(self):
        self.station_signal.emit([
            self.treeStationSearchResult.currentItem().text(0),
            self.treeStationSearchResult.currentItem().text(1)])

        return

    def station_search(self):
        search_text = self.txtSearch.text()
        search_option = self.comboSearchOption.currentText()
        results = get_stream_list(search_text, search_option)

        if results == 'error':
            QtWidgets.QMessageBox.critical(self, "Error", "Error connecting to radio-browser.info API")
            return

        if results:
            self.treeStationSearchResult.clear()
            for url in results:
                QTreeWidgetItem(self.treeStationSearchResult,[
                    url['name'],
                    url['url_resolved'],
                    url['tags'],
                    url['country'],
                    url['codec'],
                    str(url['bitrate'])])
        else:
            self.txtSearch.setText('')
            self.txtSearch.setPlaceholderText(f"No results found for {search_option}:{search_text}")