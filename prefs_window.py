from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp, QTreeWidgetItem

from lib.ui.prefs import Ui_Prefs
import functools
import io
from pathlib import Path

# config_path = f"{Path.home()}/.radioqt"

class PrefsWindow(QtWidgets.QWidget, Ui_Prefs):
    def __init__(self, parent=None,config=None,config_path=None):
        super(PrefsWindow, self).__init__(parent)
        self.setupUi(self)

        self.config = config
        self.config_path = config_path

        self.btnClose.clicked.connect(self.close_window)
        self.optBoolTooltips.clicked.connect(functools.partial(self.update_prefs, 'optBoolTooltips'))
        self.optBoolMinimized.clicked.connect(functools.partial(self.update_prefs, 'optBoolMinimized'))
        self.leStationsJSON.textEdited.connect(functools.partial(self.update_prefs, 'leStationJSON'))
        self.leFavsJSON.textEdited.connect(functools.partial(self.update_prefs, 'leFavsJSON'))

        self.load_prefs()

    def close_window(self):
        self.save_prefs()
        self.close()

    def load_prefs(self):
        self.optBoolMinimized.setChecked(self.config.getboolean('DEFAULT','optBoolMinimized'))
        self.optBoolTooltips.setChecked(self.config.getboolean('DEFAULT','optBoolTooltips'))
        self.leStationsJSON.setText(self.config['PATHS']['leStationJSON'])
        self.leFavsJSON.setText(self.config['PATHS']['leFavsJSON'])

    def update_prefs(self,field,data):
        print(f"field = {field} data = {data}")

        if field == 'optBoolTooltips':
            if data:
                self.config['DEFAULT']['optBoolTooltips'] = 'True'
            else:
                self.config['DEFAULT']['optBoolTooltips'] = 'False'

        if field == 'optBoolMinimized':
            if data:
                self.config['DEFAULT']['optBoolMinimized'] = 'True'
            else:
                self.config['DEFAULT']['optBoolMinimized'] = 'False'

        if field == 'leStationJSON':
            self.config['PATHS']['leStationJSON'] = data

        if field == 'leFavsJSON':
            self.config['PATHS']['leFavsJSON'] = data

    def save_prefs(self):
        with open(self.config_path, 'w') as configfile:    # save
            self.config.write(configfile)
