# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnToggle = QtWidgets.QPushButton(self.centralwidget)
        self.btnToggle.setGeometry(QtCore.QRect(50, 63, 31, 22))
        self.btnToggle.setText("")
        self.btnToggle.setObjectName("btnToggle")
        self.twStationList = QtWidgets.QTreeWidget(self.centralwidget)
        self.twStationList.setGeometry(QtCore.QRect(10, 112, 381, 231))
        self.twStationList.setStyleSheet("font-size: 15px;\n"
"")
        self.twStationList.setAutoScrollMargin(16)
        self.twStationList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.twStationList.setIndentation(0)
        self.twStationList.setRootIsDecorated(True)
        self.twStationList.setHeaderHidden(True)
        self.twStationList.setObjectName("twStationList")
        item_0 = QtWidgets.QTreeWidgetItem(self.twStationList)
        self.lblNowPlaying = QtWidgets.QLabel(self.centralwidget)
        self.lblNowPlaying.setGeometry(QtCore.QRect(70, 8, 321, 20))
        self.lblNowPlaying.setStyleSheet("background-color: #000000;\n"
"color: #fff;\n"
"font-weight: bold;\n"
"padding-left: 5px;")
        self.lblNowPlaying.setText("")
        self.lblNowPlaying.setObjectName("lblNowPlaying")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(8, 10, 51, 16))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(8, 40, 51, 16))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lblStationName = QtWidgets.QLabel(self.centralwidget)
        self.lblStationName.setGeometry(QtCore.QRect(70, 38, 321, 20))
        self.lblStationName.setStyleSheet("background-color: #000000;\n"
"color: #fff;\n"
"font-weight: bold;\n"
"padding-left: 5px;")
        self.lblStationName.setText("")
        self.lblStationName.setObjectName("lblStationName")
        self.btnFav = QtWidgets.QPushButton(self.centralwidget)
        self.btnFav.setGeometry(QtCore.QRect(10, 63, 31, 22))
        self.btnFav.setText("")
        self.btnFav.setObjectName("btnFav")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 350, 421, 31))
        self.frame.setStyleSheet("background-color: rgb(218, 218, 218)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lblStatus = QtWidgets.QLabel(self.frame)
        self.lblStatus.setGeometry(QtCore.QRect(20, 6, 391, 16))
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        self.btnShuffle = QtWidgets.QPushButton(self.centralwidget)
        self.btnShuffle.setGeometry(QtCore.QRect(360, 63, 31, 22))
        self.btnShuffle.setText("")
        self.btnShuffle.setObjectName("btnShuffle")
        self.sliderVolume = QtWidgets.QSlider(self.centralwidget)
        self.sliderVolume.setGeometry(QtCore.QRect(10, 90, 381, 20))
        self.sliderVolume.setSingleStep(5)
        self.sliderVolume.setProperty("value", 50)
        self.sliderVolume.setOrientation(QtCore.Qt.Horizontal)
        self.sliderVolume.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sliderVolume.setTickInterval(5)
        self.sliderVolume.setObjectName("sliderVolume")
        self.btnGetStreams = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetStreams.setGeometry(QtCore.QRect(110, 63, 111, 22))
        self.btnGetStreams.setObjectName("btnGetStreams")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.menuActionQuit = QtWidgets.QAction(MainWindow)
        self.menuActionQuit.setObjectName("menuActionQuit")
        self.actionLog = QtWidgets.QAction(MainWindow)
        self.actionLog.setObjectName("actionLog")
        self.actionAddStation = QtWidgets.QAction(MainWindow)
        self.actionAddStation.setObjectName("actionAddStation")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuActionMinimize = QtWidgets.QAction(MainWindow)
        self.menuActionMinimize.setObjectName("menuActionMinimize")
        self.actionPrefs = QtWidgets.QAction(MainWindow)
        self.actionPrefs.setObjectName("actionPrefs")
        self.actionSearch = QtWidgets.QAction(MainWindow)
        self.actionSearch.setObjectName("actionSearch")
        self.menuFile.addAction(self.menuActionMinimize)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuActionQuit)
        self.menuView.addAction(self.actionLog)
        self.menuView.addAction(self.actionSearch)
        self.menuView.addAction(self.actionAddStation)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionPrefs)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.twStationList.headerItem().setText(0, _translate("MainWindow", "Stataion Name"))
        self.twStationList.headerItem().setText(1, _translate("MainWindow", "URL"))
        __sortingEnabled = self.twStationList.isSortingEnabled()
        self.twStationList.setSortingEnabled(False)
        self.twStationList.topLevelItem(0).setText(0, _translate("MainWindow", "New Item"))
        self.twStationList.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Playing"))
        self.label_2.setText(_translate("MainWindow", "Station"))
        self.btnGetStreams.setText(_translate("MainWindow", "Get Streams"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "Options"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuActionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionLog.setText(_translate("MainWindow", "Favorites"))
        self.actionAddStation.setText(_translate("MainWindow", "Add Station"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize to Tray"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.menuActionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionPrefs.setText(_translate("MainWindow", "Preferences"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
