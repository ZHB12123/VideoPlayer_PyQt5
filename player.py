import sys

from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia,QtMultimediaWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from player_ui import Ui_PlayerForm
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer

class MyMainForm(QMainWindow,Ui_PlayerForm):
    def __init__(self, parent=None):
        super(MyMainForm,self).__init__(parent)
        self.setupUi(self)

        self.PauseButton.clicked.connect(self.VideoPause)
        self.PlayButton.clicked.connect(self.VideoPlay)
        self.StopButton.clicked.connect(self.VideoStop)
        self.FileOpen.clicked.connect(self.OpenVideo)

        self.videoLen=0

        self.timer=QTimer(self)
        self.timer.timeout.connect(self.Operate)
        self.timer.start(100)

        self.setFocusPolicy(Qt.ClickFocus)#通过鼠标点击可以转移焦点。
        self.OpenVideo()
        
        self.ProgressBar.setMinimum(0)
        self.ProgressBar.setMaximum(10000)
        

    def OpenVideo(self):
        File=QtWidgets.QFileDialog.getOpenFileUrl()[0]
        self.player.setMedia(QtMultimedia.QMediaContent(File)) #打开视频，获得将要播放的视频的路径。
        self.VideoPlay()
        #help(File)
        self.setWindowTitle(File.fileName())

    def VideoPause(self):
        self.player.pause()
        self.vw.setFocus()#将焦点转移至视频播放页面方便监听键盘的空格键事件。
        
        pass

    def VideoPlay(self):
        self.player.play()
        self.vw.setFocus()#将焦点转移至视频播放页面方便监听键盘的空格键事件。
        print(self.player.position())
        if self.player.position()<=500:
            self.videoLen=self.player.duration()
            print(self.videoLen)
        pass
    
    def VideoStop(self):
        self.player.stop()
        self.vw.setFocus()#将焦点转移至视频播放页面方便监听键盘的空格键事件。
        pass
    
    def Operate(self):
        t=self.player.position()
        self.PlayTime.setNum(t/1000)
        if self.player.duration()!=0:
            self.ProgressBar.setValue(int(t/self.player.duration()*10000))

    def keyPressEvent(self,evt):
        
        #print(evt.key())
        
        if evt.key()==Qt.Key_Space and self.player.state()==1:
            self.player.pause()
            
        elif evt.key()==Qt.Key_Space and self.player.state()==2:
            self.player.play()
               
        elif evt.key()==Qt.Key_Right:
            self.player.setPosition(self.player.position()+1000)
        
        elif evt.key()==Qt.Key_Left:
            self.player.setPosition(self.player.position()-1000)

        pass
        
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    mywin=MyMainForm()
    mywin.show()
    sys.exit(app.exec_())