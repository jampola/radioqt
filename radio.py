#!/usr/bin/python3
import os.path
import vlc
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction, QTreeWidgetItem
import sys
import time
from pathlib import Path
import datetime
import json
import functools
import configparser
from random import shuffle
from os import path,environ

from lib.get_meta import streamscrobbler
from lib.get_artwork import get_artwork_by_title_artist
from lib.ui.mainwindow import Ui_MainWindow

from log_window import LogWindow
from add_station import AddStationWindow
from about_window import AboutWindow
from prefs_window import PrefsWindow
from search_window import SearchWindow

config = configparser.RawConfigParser(allow_no_value=True)

# Ensure VLC knows where it's looking for the libs
environ["VLC_PLUGIN_PATH"] = "/usr/lib/x86_64-linux-gnu/"

# Try look for a user config and set defaults if needed
HOMEDIR = Path.home()

if not path.exists(f"{HOMEDIR}/.config/radioqt/radioqt.ini"):
    config_path = "/etc/radioqt.ini"
else:
    config_path = f"{HOMEDIR}/.config/radioqt/radioqt.ini"

config.read(config_path)

FAVORITES = os.path.expanduser(config['PATHS']['lefavsjson'])
STATIONS = os.path.expanduser(config['PATHS']['lestationjson'])

def _check_json_files_exist(filename):
    """ Check if the required json files exist, if not, create empty ones
    """
    if not path.exists(filename):
        print(f"file {filename} does not exist, creating...")

        with open(filename,'w+') as outfile:
            outfile.write("{}")

# Check if the file exists, if not, create it
_check_json_files_exist(FAVORITES)
_check_json_files_exist(STATIONS)

with open(FAVORITES) as fav_json_file:
    favorite_list = json.load(fav_json_file)

with open(STATIONS) as station_json_file:
    playlist_urls = json.load(station_json_file)

class GetMetaWorker(QThread):
    """ This is responsible for pulling song meta data and passing
    it to our UI
    """
    signal = pyqtSignal(dict)

    def __init__(self):
        QThread.__init__(self)
        self.running = True
        self.url = ""
        self.song = ""
        self.last_song = ""
        self.ss = streamscrobbler()

    def stop_thread(self,data):
        if data:
            self.running = False

    def on_message_from_main(self,data):
        self.url = data
        self.running = True

    # This runs ALL THE TIME
    def run(self):
        """ Start the thread that gets our meta
        """
        time.sleep(1)
        while True:
            time.sleep(1)
            if self.running:
                art = False
                try:
                    self.song = self.ss.getAllData(address=self.url)['metadata']['song']
                except:
                    self.song = "Unable to fetch song meta data"

                try:
                    if self.last_song != self.song:
                        artist = self.song.split('-')[0]
                        title = self.song.split('-')[1]
                        art = get_artwork_by_title_artist(artist,title)
                    else:
                        art = True
                except:
                    pass

                self.last_song = self.song
                self.signal.emit({'title': self.song, 'has_art': art})

                time.sleep(5)
            else:
                return

class UpdateStatusWorker(QThread):
    """ Update the status label
    """
    signal = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

        self.status_message = ""
        self.running = False

    def on_message_from_main(self,data):
        if self.running:
            return
        self.status_message = data
        self.running = True

    def run(self):
        while True:
            time.sleep(.1)
            if self.running:
                self.signal.emit(self.status_message)
                time.sleep(2)
                self.signal.emit('Playing')
                self.running = False

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    url_signal = pyqtSignal(str)
    meta_start_stop_signal = pyqtSignal(str)
    selected_station_signal = pyqtSignal(tuple)
    update_status_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.playing = False
        self.song_pos = None
        self.currently_playing = None
        self.station_name = ""
        self.station_url = ""
        self.playlist_urls_sorted = {}

        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()

        self.setupUi(self)

        # Tray Icon
        self.tray_icon = QSystemTrayIcon(self)
        self.icon = QtGui.QIcon('/usr/share/radioqt/icons/systray.png')

        tray_menu = QMenu()
        self.tray_icon.setIcon(self.icon)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        self.app_show = False # keep a track if the app is shown

        # Config options
        self.app_start_minimized = config.getboolean('DEFAULT','optBoolMinimized') # keep a track if the app is shown
        self.show_song_tooltips = config.getboolean('DEFAULT','optbooltooltips') # Show the song tooltips in tray

        # Assign actions for tray
        fave_action = QAction("Add to Favorites", self)
        quit_action = QAction("Exit", self)

        quit_action.triggered.connect(self.quit_app)
        fave_action.triggered.connect(self.add_favorite)

        tray_menu.addAction(fave_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.activated.connect(self.show_hide_app)

        self.recreate_playlist()

        # Connect get meta object
        self.get_meta = GetMetaWorker()
        self.url_signal.connect(self.get_meta.on_message_from_main)
        self.meta_start_stop_signal.connect(self.get_meta.stop_thread)
        self.get_meta.signal.connect(self.display_meta)

        #  Connect update status object
        self.update_status = UpdateStatusWorker()
        self.update_status.signal.connect(self.render_status)
        self.update_status_signal.connect(self.update_status.on_message_from_main)

        # Connect other windows
        self.logform = LogWindow(config=config,favorites=FAVORITES)
        self.about = AboutWindow()

        self.search_window = SearchWindow()
        self.search_window.station_signal.connect(self.add_to_playlist)

        self.prefs = PrefsWindow(config=config,config_path=config_path)

        self.add_station = AddStationWindow()
        self.add_station.station_signal.connect(self.add_to_playlist)
        self.selected_station_signal.connect(self.add_station.edit_station)

        # Connecting button
        self.sliderVolume.valueChanged.connect(self.adjust_volume)
        self.btnToggle.clicked.connect(self.play_toggle)
        self.btnShuffle.clicked.connect(functools.partial(self.play_station,shuffle_url=True))
        self.twStationList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.twStationList.customContextMenuRequested.connect(self.menu_context_tree)
        self.twStationList.doubleClicked.connect(functools.partial(self.play_station,shuffle_url=False))
        self.actionLog.triggered.connect(self.show_log_window)
        self.actionPrefs.triggered.connect(self.show_prefs_window)
        self.menuActionQuit.triggered.connect(self.quit_app)
        self.actionAddStation.triggered.connect(self.show_addstation_window)
        self.actionAbout.triggered.connect(self.show_about_window)
        self.actionSearch.triggered.connect(self.show_search_window)
        self.btnFav.clicked.connect(self.add_favorite)
        # self.actionMinimize.triggered.connect(self.hide)
        self.menuActionMinimize.triggered.connect(self.show_hide_app)

        self.playback_start_icon = QtGui.QIcon("/usr/share/radioqt/icons/media-playback-start.png")
        self.playback_stop_icon = QtGui.QIcon("/usr/share/radioqt/icons/media-playback-stop.png")
        self.shuffle_station = QtGui.QIcon("/usr/share/radioqt/icons/media-playlist-shuffle.png")
        self.button_favorite = QtGui.QIcon("/usr/share/radioqt/icons/emblem-favorite.png")

        self._set_default_artwork()

        self.btnFav.setIcon(self.button_favorite)
        self.btnToggle.setIcon(self.playback_start_icon)
        self.btnShuffle.setIcon(self.shuffle_station)

        self.twStationList.hideColumn(1)

        # Optional, resize window to image size
        self.resize(96,96)

        # Finally show the app if configured to
        if not self.app_start_minimized:
            self.show_hide_app('show')

    def show_log_window(self):
        self.w = LogWindow(config=config,favorites=FAVORITES)
        self.w.show()

    def show_prefs_window(self):
        self.prefs.show()

    def show_addstation_window(self):
        self.add_station.show()

    def show_about_window(self):
        self.about.show()

    def show_search_window(self):
        self.search_window.show()

    def quit_app(self):
        sys.exit()

    def show_hide_app(self, reason=None):
        if not reason:
            if self.app_show:
                self.hide()
                self.app_show = False
            else:
                self.show()
                self.app_show = True

        if reason == 2:
            if self.app_show:
                self.hide()
                self.app_show = False
            else:
                self.show()
                self.app_show = True

        elif reason == 'show': # Called from configparser options
            self.show()
            self.app_show = True

    def add_favorite(self):
        self.update_status.start()

        if self.currently_playing:
            s_list = [x for x in favorite_list]
            if self.currently_playing not in s_list:
                favorite_list[self.currently_playing] = str(datetime.datetime.now().date())
                with open(FAVORITES, 'w') as outfile:
                    json.dump(favorite_list, outfile)

            self.update_status_signal.emit("<b style='color:green;'>Song added to favorites</b>")

    def set_starting_volume(self):
        self.sliderVolume.setValue(self.mediaplayer.audio_get_volume())

    def recreate_playlist(self,add=False):
        self.twStationList.clear()

        # Sorted on the fly
        # ToDo: Sort using header in UI
        self.playlist_urls_sorted = {
            k: v for k, v in sorted(playlist_urls.items(), key=lambda item: item[1])
            }

        for x in self.playlist_urls_sorted:
            QTreeWidgetItem(self.twStationList,[playlist_urls[x],x])

        if add:
            pass

    def menu_context_tree(self, event):
        self.menu_contextuelAlb = QtWidgets.QMenu(self.twStationList)

        delete_action = self.menu_contextuelAlb.addAction("Delete")
        edit_action = self.menu_contextuelAlb.addAction("Edit")
        action_menu = self.menu_contextuelAlb.exec_(self.twStationList.mapToGlobal(event))

        if action_menu is not None:
            if action_menu == delete_action:
                self.remove_station()

            if action_menu == edit_action:
                self.show_addstation_window()
                self.selected_station_signal.emit(self._get_selected_station())

    def display_meta(self,data):
        if self.playing:
            if 'title' in data:
                self.lblNowPlaying.setText(data['title'])
                if self.currently_playing != data['title']:
                    self.tray_icon.setToolTip(data['title'])

                    # Show tooltip popups on song
                    if self.show_song_tooltips:
                        self.tray_icon.showMessage("RadIO",f"{data['title']}",msecs=2000)

                self.currently_playing = data['title']
                self.set_starting_volume()

                # todo: explicitly check if artwork is available
                if data.get('has_art'):
                    self.now_playing = QtGui.QPixmap("/tmp/radioimg.jpg")
                    scaled = self.now_playing.scaled(128,128)
                    self.lblStationImage.setPixmap(scaled)
                else:
                    self._set_default_artwork()
        else:
            self.lblNowPlaying.setText("Nothing Playing")
            self.lblNowStationName.setText("")

    def add_to_playlist(self,data):
        self.station_name = data[0]
        self.station_url = data[1]
        # Now add this to the TreeView List
        QTreeWidgetItem(self.twStationList,[self.station_name,self.station_url])
        playlist_urls[self.station_url] = self.station_name

        with open(STATIONS, 'w') as outfile:
            json.dump(playlist_urls, outfile)

        self.recreate_playlist(add=True)

    def remove_station(self):
        root = self.twStationList.invisibleRootItem()
        for item in self.twStationList.selectedItems():
            del playlist_urls[item.text(1)]
            (item.parent() or root).removeChild(item)

        with open(STATIONS, 'w') as outfile:
            json.dump(playlist_urls, outfile)

        self.recreate_playlist()

    def _set_default_artwork(self):
        self.now_playing = QtGui.QPixmap("/usr/share/radioqt/pixmaps/noart.png")
        scaled = self.now_playing.scaled(128, 128)
        self.lblStationImage.setPixmap(scaled)

    def _get_selected_station(self):
        getSelected = self.twStationList.selectedItems()
        baseNode = getSelected[0]
        station_name = baseNode.text(0)
        station_url = baseNode.text(1)

        return station_name,station_url

    def render_status(self,data):
        self.lblStatus.setText(data)

    def play_station(self,shuffle_url=False):
        self.get_meta.start()

        self.lblNowPlaying.setText("Loading...")

        # Shuffle the urls as keys
        if shuffle_url:
            keys = list(self.playlist_urls_sorted.keys())
            shuffle(keys)
            station_name,station_url = self.playlist_urls_sorted[keys[0]],keys[0]
            self.recreate_playlist()
        else:
            station_name,station_url = self._get_selected_station()

        # Emit the URL to our metadata worker
        self.url_signal.emit(station_url)

        self.url = station_url
        self.media = self.instance.media_new(station_url)
        self.media.parse()
        self.mediaplayer.set_media(self.media)
        self.mediaplayer.play()
        self.playing = True
        self.btnToggle.setIcon(self.playback_stop_icon)
        self.lblStationName.setText(station_name)
        self.lblStatus.setText('Playing')

    def set_volume(self, vol_val):
        self.mediaplayer.audio_set_volume(vol_val)

    def adjust_volume(self):
        self.set_volume(self.sliderVolume.value())

    def play_toggle(self):
        if self.mediaplayer.is_playing():
            self.mediaplayer.stop()
            self.meta_start_stop_signal.emit("stop")
            self.btnToggle.setIcon(self.playback_start_icon)
            self.lblStationName.setText('No Station')
            self.lblNowPlaying.setText('Not Playing')
            self.lblStatus.setText('Stopped')
            self._set_default_artwork()

    def closeEvent(self,e):
        self.get_meta.stop_thread()
        sys.exit()

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    # form.show()
    app.exec_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
