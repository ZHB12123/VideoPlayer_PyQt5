# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia,QtMultimediaWidgets
from PyQt5.QtWidgets import QAbstractItemView,QTableWidgetItem,QApplication

class SubBox():
    def __init__(self,Form):
        self.line1=QtWidgets.QLabel(Form)
        self.line1.setObjectName("line1")
        self.line1.setStyleSheet("QLabel{background-color:rgba(55, 255, 55, 100%);border:none;}")

        self.line2=QtWidgets.QLabel(Form)
        self.line2.setObjectName("line2")
        self.line2.setStyleSheet("QLabel{background-color:rgba(55, 255, 55, 100%);border:none;}")

        self.line3=QtWidgets.QLabel(Form)
        self.line3.setObjectName("line3")
        self.line3.setStyleSheet("QLabel{background-color:rgba(55, 255, 55, 100%);border:none;}")

        self.line4=QtWidgets.QLabel(Form)
        self.line4.setObjectName("line4")
        self.line4.setStyleSheet("QLabel{background-color:rgba(55, 255, 55, 100%);border:none;}")

    def setParameters(self,x,y,width,height):
        self.line1.setGeometry(QtCore.QRect(x, y, width, 1))
        self.line2.setGeometry(QtCore.QRect(x, y+height, width, 1))
        self.line3.setGeometry(QtCore.QRect(x, y, 1, height))
        self.line4.setGeometry(QtCore.QRect(x+width, y, 1, height))

class VideoView(QtMultimediaWidgets.QVideoWidget):  #包含在视频上画框的功能
    def __init__(self,Form):
        super(VideoView,self).__init__(Form)
        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        self.flag = False
        self.SubtitleBox=SubBox(Form)
        self.SubtitleBox.setParameters(0,0,0,0)
    #鼠标点击事件
    def mousePressEvent(self,event):
        self.flag = True
        self.x0 = event.x()+self.x()
        self.y0 = event.y()+self.y()
        self.SubtitleBox.setParameters(0,0,0,0)
        
    #鼠标释放事件
    def mouseReleaseEvent(self,event):
        self.flag = False
        self.update()
        
    #鼠标移动事件
    def mouseMoveEvent(self,event):
        if self.flag:
            self.x1 = event.x()+self.x()
            self.y1 = event.y()+self.y()
            self.SubtitleBox.setParameters(self.x0,self.y0,self.x1-self.x0,self.y1-self.y0)


class Ui_PlayerForm(object):
    def setupUi(self, PlayerForm):
        PlayerForm.setObjectName("PlayerForm")
        desktop = QApplication.desktop()
        PlayerForm.resize(desktop.width()-200, desktop.height()-100)

        self.vw = VideoView(PlayerForm)
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

        self.SaveLine = QtWidgets.QPushButton(PlayerForm)
        self.SaveLine.setGeometry(QtCore.QRect(1370, 820, 75, 25))
        self.SaveLine.setObjectName("SaveLine")

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
        self.SaveLine.setText(_translate("Form", "SaveLine"))
