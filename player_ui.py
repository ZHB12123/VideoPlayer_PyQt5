# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia,QtMultimediaWidgets
from PyQt5.QtWidgets import QAbstractItemView,QTableWidgetItem,QApplication

class Ui_PlayerForm(object):
    def setupUi(self, PlayerForm):
        PlayerForm.setObjectName("PlayerForm")
        desktop = QApplication.desktop()
        PlayerForm.resize(desktop.width()-200, desktop.height()-100)

        self.vw = QtMultimediaWidgets.QVideoWidget(PlayerForm)
        self.vw.setGeometry(QtCore.QRect(10, 10, 1280, 720))
        self.vw.setObjectName("graphicsView")
        self.vw.show()
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setVideoOutput(self.vw)

        self.splitter = QtWidgets.QSplitter(PlayerForm)
        self.splitter.setGeometry(QtCore.QRect(500, 780, 250, 30))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.PauseButton = QtWidgets.QPushButton(self.splitter)
        self.PauseButton.setObjectName("Pause")
        self.PlayButton = QtWidgets.QPushButton(self.splitter)
        self.PlayButton.setObjectName("Play")
        self.StopButton = QtWidgets.QPushButton(self.splitter)
        self.StopButton.setObjectName("Stop")

        self.splitter_2 = QtWidgets.QSplitter(PlayerForm)
        self.splitter_2.setGeometry(QtCore.QRect(500, 820, 250, 30))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.SubStart = QtWidgets.QPushButton(self.splitter_2)
        self.SubStart.setObjectName("SubStart")
        self.SubEnd = QtWidgets.QPushButton(self.splitter_2)
        self.SubEnd.setObjectName("SubEnd")
        self.SubConfirm = QtWidgets.QPushButton(self.splitter_2)
        self.SubConfirm.setObjectName("OK")

        self.splitter_3=QtWidgets.QSplitter(PlayerForm)
        self.splitter_3.setGeometry(QtCore.QRect(505, 850, 160, 30))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_3")
        self.StartTime = QtWidgets.QLabel(self.splitter_3)
        self.StartTime.setObjectName("StartTime")
        self.EndTime = QtWidgets.QLabel(self.splitter_3)
        self.EndTime.setObjectName("EndTime")

        self.ProgressBar = QtWidgets.QSlider(PlayerForm)
        self.ProgressBar.setGeometry(QtCore.QRect(10, 740, 1280, 20))
        self.ProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.ProgressBar.setObjectName("ProgressBar")
    
        self.FileOpen = QtWidgets.QPushButton(PlayerForm)
        self.FileOpen.setGeometry(QtCore.QRect(10, 800, 75, 30))
        self.FileOpen.setObjectName("FileOpen")

        self.PlayTime = QtWidgets.QLabel(PlayerForm)
        self.PlayTime.setGeometry(QtCore.QRect(20, 770, 55, 20))
        self.PlayTime.setObjectName("0.00")
        #表格
        self.TimeTable = QtWidgets.QTableWidget(PlayerForm)
        self.TimeTable.setGeometry(QtCore.QRect(1300, 10, 220, 750))
        self.TimeTable.setObjectName("TimeTable")
        self.TimeTable.setColumnCount(2)
        self.TimeTable.setRowCount(0)
        #self.TimeTable.setColumnWidth(0,88)
        #self.TimeTable.setColumnWidth(1,88)
        self.TimeTable.setShowGrid(True)
        self.TimeTable.setHorizontalHeaderLabels(['Start','End'])
        self.TimeTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.DelLine = QtWidgets.QPushButton(PlayerForm)
        self.DelLine.setGeometry(QtCore.QRect(1370, 780, 75, 25))
        self.DelLine.setObjectName("DelLine")

        self.retranslateUi(PlayerForm)
        QtCore.QMetaObject.connectSlotsByName(PlayerForm)

    def retranslateUi(self, PlayerForm):
        _translate = QtCore.QCoreApplication.translate
        PlayerForm.setWindowTitle(_translate("PlayerForm", "Form"))
        self.PlayButton.setText(_translate("PlayerForm", "Play"))
        self.StopButton.setText(_translate("PlayerForm", "Stop"))
        self.PauseButton.setText(_translate("PlayerForm", "Pause"))
        self.FileOpen.setText(_translate("PlayerForm", "OPEN"))
        self.SubStart.setText(_translate("PlayerForm", "SubStart"))
        self.SubEnd.setText(_translate("PlayerForm", "SubEnd"))
        self.SubConfirm.setText(_translate("PlayerForm", "SubConfirm"))
        self.StartTime.setText(_translate("PlayerForm", ""))
        self.EndTime.setText(_translate("PlayerForm", ""))
        self.PlayTime.setText(_translate("PlayerForm", "TextLabel"))
        self.DelLine.setText(_translate("Form", "DelLine"))