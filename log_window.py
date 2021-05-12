import json
import datetime
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp, QTreeWidgetItem

import webbrowser
import configparser
from pathlib import Path


from lib.ui.logwindow import Ui_Form

# config = configparser.RawConfigParser(allow_no_value=True)
# config_path = f"{Path.home()}/.radioqt.ini"
# config.read(config_path)

# FAVORITES = config['PATHS']['lefavsjson']

# with open(FAVORITES) as fav_json_file:
#     favorite_list = json.load(fav_json_file)

class LogWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None, config=None, favorites=None):
        super(LogWindow, self).__init__(parent)

        self.config = config
        # self.favorites = config['PATHS']['lefavsjson']
        self.favorites = favorites

        self.titles = []
        self.setupUi(self)
        self.populate_favorites()
        self.twSongLog.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.twSongLog.customContextMenuRequested.connect(self.menu_context_tree)
        self.btnFindYouTube.clicked.connect(self.search_song)
        self.btnCloseFavorites.clicked.connect(self.close)
        self.twSongLog.hideColumn(0)

    def menu_context_tree(self, event):
        self.menu_contextuelAlb = QtWidgets.QMenu(self.twSongLog)
        delete_action = self.menu_contextuelAlb.addAction("Delete")
        find_action = self.menu_contextuelAlb.addAction("Find on YouTube")
        action_menu = self.menu_contextuelAlb.exec_(self.twSongLog.mapToGlobal(event))

        if action_menu is not None:
            if action_menu == delete_action:
                self.remove_favorite()

            if action_menu == find_action:
                self.search_song()

    def search_song(self):
        root = self.twSongLog.invisibleRootItem()
        for item in self.twSongLog.selectedItems():
            url="https://www.youtube.com/results?search_query={}".format(item.text(1).replace(" ","+"))
            webbrowser.open(url)

    def _open_fav_list(self):
        with open(self.favorites) as fav_json_file:
            favorite_list = json.load(fav_json_file)
        return favorite_list

    def remove_favorite(self):
        favorite_list = self._open_fav_list()

        root = self.twSongLog.invisibleRootItem()
        for item in self.twSongLog.selectedItems():
            del favorite_list[item.text(1)] # remove stations from loaded dict
            (item.parent() or root).removeChild(item)

        with open(self.favorites, 'w') as outfile:
            json.dump(favorite_list, outfile)

    def populate_favorites(self):
        favorite_list = self._open_fav_list()

        for song in favorite_list:
            QTreeWidgetItem(self.twSongLog,[str(datetime.datetime.now().date()),str(song)])