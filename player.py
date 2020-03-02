import sys
from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia,QtMultimediaWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QAbstractItemView,QTableWidgetItem
from player_ui import Ui_PlayerForm
from PyQt5.QtCore import Qt,QRect
from PyQt5.QtCore import QTimer

class MyMainForm(QMainWindow,Ui_PlayerForm):
    def __init__(self, parent=None):
        super(MyMainForm,self).__init__(parent)
        self.setupUi(self)
        self.setMinimumSize(1530/2,900/2)

        self.PauseButton.clicked.connect(self.VideoPause)
        self.PlayButton.clicked.connect(self.VideoPlay)
        self.StopButton.clicked.connect(self.VideoStop)
        self.FileOpen.clicked.connect(self.OpenVideo)
        self.SubStart.clicked.connect(self._SubStart)
        self.SubEnd.clicked.connect(self._SubEnd)
        self.SubConfirm.clicked.connect(self._SubConfirm)

        self.timer1=QTimer(self)
        self.timer1.timeout.connect(self.TimeText)
        self.timer2=QTimer(self)
        self.timer2.timeout.connect(self.TimeBar)

        self.ProgressBar.sliderPressed.connect(self.SliderPre)
        self.ProgressBar.sliderReleased.connect(self.SliderRel)
        self.ProgressBar.sliderMoved.connect(self.SliderMov)

        self.TimeTable.setFocusPolicy(Qt.NoFocus)
        self.DelLine.clicked.connect(self.DeleteLine)
        self.SaveLine.clicked.connect(self.SaveSubTimeline)

        self.setFocusPolicy(Qt.ClickFocus)  #通过鼠标点击可以转移焦点。

        self.FileName=""
        self.OpenVideo()
        
        self.ProgressBar.setMinimum(0)
        self.ProgressBar.setMaximum(10000)
        
        self.VideoStatus=1

        self.SubData=[]
        self.SubStartPoint=0
        self.SubEndPoint=0
        self.SubNum=1
        

    def resizeEvent(self,evt):  #当窗口大小改变时触发
        self.vw.setGeometry(self.width()*10/1530,self.height()*10/900,self.width()*1280/1530,self.height()*720/900)
        self.splitter.setGeometry(self.width()*500/1530,self.height()*780/900,self.width()*250/1530,self.height()*30/900)
        self.splitter_2.setGeometry(self.width()*500/1530,self.height()*820/900,self.width()*250/1530,self.height()*30/900)
        self.splitter_3.setGeometry(self.width()*505/1530,self.height()*850/900,self.width()*160/1530,self.height()*30/900)
        self.ProgressBar.setGeometry(self.width()*10/1530,self.height()*740/900,self.width()*1280/1530,self.height()*20/900)
        self.FileOpen.setGeometry(self.width()*10/1530,self.height()*800/900,self.width()*75/1530,self.height()*30/900)
        self.PlayTime.setGeometry(self.width()*20/1530,self.height()*770/900,self.width()*55/1530,self.height()*20/900)
        self.TimeTable.setGeometry(self.width()*1300/1530,self.height()*10/900,self.width()*220/1530,self.height()*750/900)
        self.DelLine.setGeometry(self.width()*1370/1530,self.height()*780/900,self.width()*75/1530,self.height()*25/900)
        self.SaveLine.setGeometry(self.width()*1370/1530,self.height()*820/900,self.width()*75/1530,self.height()*25/900)

    def OpenVideo(self):
        File=QtWidgets.QFileDialog.getOpenFileUrl()[0]
        
        if File.fileName()!='':
            self.player.setMedia(QtMultimedia.QMediaContent(File)) #打开视频，获得将要播放的视频的路径。
            self.timer1.start(100)
            self.timer2.start(100)
            self.VideoPlay()
            self.setWindowTitle(File.fileName())
            self.FileName=File.fileName()
            print(self.FileName)


    def VideoPause(self):
        self.player.pause()
        self.vw.setFocus()#将焦点转移至视频播放页面方便监听键盘的空格键事件。
        pass

    def VideoPlay(self):
        self.player.play()
        self.vw.setFocus()#将焦点转移至视频播放页面方便监听键盘的空格键事件。
        pass
    
    def VideoStop(self):
        self.player.stop()
        self.vw.setFocus()#将焦点转移至视频播放页面方便监听键盘的空格键事件。
        pass
    
    def TimeText(self):
        t=self.player.position()
        self.PlayTime.setNum(t/1000)
    
    #进度条部分
    def SliderPre(self):
        self.timer2.stop()
        if self.player.state()==1:
            self.player.pause()
            self.VideoStatus=1
        elif self.player.state()==2:
            self.VideoStatus=2
        pass
    def SliderRel(self):    
        self.timer2.start(100)
        if self.VideoStatus==1:
            self.player.play()
        if self.VideoStatus==2:
            self.player.pause()
        self.vw.setFocus()
        pass 
    def SliderMov(self):
        pos=self.ProgressBar.value()
        self.player.setPosition(int(pos/10000*self.player.duration()))
        pass
    def TimeBar(self):
        t=self.player.position()
        if self.player.duration()!=0:
            self.ProgressBar.setValue(int(t/self.player.duration()*10000))

    def _SubStart(self):
        self.SubStartPoint=self.player.position()
        self.StartTime.setText(str(self.SubStartPoint))
        self.vw.setFocus()
        pass
    def _SubEnd(self):
        self.SubEndPoint=self.player.position()
        self.EndTime.setText(str(self.SubEndPoint))
        self.vw.setFocus()
        pass
    def _SubConfirm(self):
        if self.SubEndPoint>self.SubStartPoint:
            self.SubData.append([self.SubStartPoint,self.SubEndPoint,self.vw.x0+self.vw.x(),self.vw.y0-self.vw.y(),\
                self.vw.x1+self.vw.x(),self.vw.y1-self.vw.y(),self.vw.width(),self.vw.height()])
            row = self.TimeTable.rowCount()
            self.TimeTable.insertRow(row)
            item_start=QTableWidgetItem(str(self.SubStartPoint))
            item_end=QTableWidgetItem(str(self.SubEndPoint))
            self.TimeTable.setItem(row,0,item_start)
            self.TimeTable.setItem(row,1,item_end)
            self.SubNum+=1
        
        self.vw.setFocus()
        pass

    def DeleteLine(self):
        try:
            row = self.TimeTable.selectedItems()[0].row()             #获取选中文本所在的行
            column = self.TimeTable.selectedItems()[0].column()       #获取选中文本所在的列
            self.TimeTable.removeRow(row)
            del(self.SubData[row])
            self.vw.setFocus()
        except:
            pass
    def SaveSubTimeline(self):
        print(self.FileName)
        with open(self.FileName+".csv","w") as f:
            f.write("StartTime,EndTime,x0,y0,x1,y1,width,height,\n")
        with open(self.FileName+".csv","a") as f:
            for data in self.SubData:
                f.write(str(data[0])+","+str(data[1])+","+str(data[2])+","+str(data[3])+","+str(data[4])+\
                    ","+str(data[5])+","+str(data[6])+","+str(data[7])+",\n")
        pass

    def keyPressEvent(self,evt):
        #print(evt.key())
        if evt.key()==Qt.Key_Space and self.player.state()==1:
            self.player.pause()
            
        elif evt.key()==Qt.Key_Space and self.player.state()==2:
            self.player.play()
               
        elif evt.key()==Qt.Key_Right:
            self.player.setPosition(self.player.position()+50)
        
        elif evt.key()==Qt.Key_Left:
            self.player.setPosition(self.player.position()-50)
        
        elif evt.key()==Qt.Key_Up:
            self.player.setPosition(self.player.position()+250)
        
        elif evt.key()==Qt.Key_Down:
            self.player.setPosition(self.player.position()-250)
        pass
        
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    mywin=MyMainForm()
    mywin.show()
    sys.exit(app.exec_())