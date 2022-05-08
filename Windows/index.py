from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
import os
from os import path
from os.path import basename
import sys
import urllib.request
import urllib.response
from urllib.request import urlopen
import pafy
import humanize
from decimal import Decimal
from datetime import datetime, timedelta
import time
FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"AutoDownloader.ui"))
FORM_CLASS2,_=loadUiType(path.join(path.dirname(__file__),"downloadpage.ui"))
FORM_CLASS3,_=loadUiType(path.join(path.dirname(__file__),"downloadvideo.ui"))
FORM_CLASS4,_=loadUiType(path.join(path.dirname(__file__),"downloadplaylist.ui"))
def startdownload():
    global dowloader
    global counter
    global pageofdownload
    global listofdownloadwindows
    listofdownloadwindows.append('downloadwindow{}'.format(counter))
    listofdownloadwindows[counter]=pageofdownload()
    listofdownloadwindows[counter].show()
    QApplication.processEvents()
    counter += 1
def startvideo():
    global dowloader
    global counter2
    global pageofvideodownload
    global listofdownloadvideowindows
    listofdownloadvideowindows.append('downloadwindow2{}'.format(counter2))
    listofdownloadvideowindows[counter2]=pageofvideodownload()
    listofdownloadvideowindows[counter2].show()
    QApplication.processEvents()
    counter2 += 1
def startplaylist():
    global listofdownloadplaylistwindows
    global counter3
    global dowloader
    global pageofplaylistdownload
    listofdownloadplaylistwindows.append('downloadwindow3{}'.format(counter3))
    listofdownloadplaylistwindows[counter3] = pageofplaylistdownload()
    listofdownloadplaylistwindows[counter3].show()
    QApplication.processEvents()
    counter3 += 1
class dowloader(QMainWindow,FORM_CLASS):
    def __init__(self,parent=None):
        super(dowloader,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.tab = self.tabWidget
        self.setFixedSize(533, 294)
        self.tab.setFixedSize(511, 241)
        self.tab.currentChanged.connect(self.hande_size)
        self.handle_buttons()
        self.handle_savedlocation()
        self.handle_savedlocationforvideo()
        self.handle_savedlocationforplaylist()
        self.actionExit.triggered.connect(exit)
        self.actionExit.setShortcut('Ctrl+w')
    def hande_size(self):
        if self.tab.currentIndex() == 0:
            self.setFixedSize(533, 294)
            self.tab.setFixedSize(511, 241)
        if self.tab.currentIndex() == 1:
            self.setFixedSize(533, 336)
            self.tab.setFixedSize(511, 281)
        if self.tab.currentIndex() == 2:
            self.setFixedSize(533,435)
            self.tab.setFixedSize(511,381)
    def handle_buttons(self):
        self.browsebtn.clicked.connect(self.handle_browse)
        self.browsebtn_2.clicked.connect(self.handle_browse_forvid)
        self.download_btn.clicked.connect(self.savelocation)
        self.check_btn.clicked.connect(self.vidcheck)
        self.download_btn_2.clicked.connect(self.savelocationforvideo)
        self.check_btn_4.clicked.connect(self.playlistcheck)
        self.browsebtn_7.clicked.connect(self.handle_browse_forplaylist)
        self.pushButton.clicked.connect(self.playlistgetselectedvideoquality)
        self.download_btn_7.clicked.connect(self.savelocationforplaylist)
    def savelocation(self):
        global startdownload
        if self.urllineedit.text() == '' :
            QMessageBox.warning(self,'Error','you must enter a valid url')
        elif self.savelocationlineedit.text()=='':
            QMessageBox.warning(self,'Error','use browse button to select valid save location')
        else :
            if self.locationcheck.isChecked():
                self.handle_locationsaved()
            self.urllineedit.setText('')
            self.savelocationlineedit.setText('')
            self.filenamelineedit.setText('')
            startdownload()
    def handle_browse(self):
        global save_location
        global url
        global filename
        global location
        url = self.urllineedit.text()
        #try:
        self.response = urlopen(url)
        self.filetitle = basename(self.response.url)
        self.filepath = '{}/{}'.format(self.path,self.filetitle)
        location = QFileDialog.getSaveFileName(self, caption='Choose location to save your download',directory=self.filepath, filter='All files(*.*)', )
        location = location[0]
        filename = location.split('/')[-1]
        location = '/'.join(location.split('/')[:-1])
        self.filenamelineedit.setText(filename)
        self.savelocationlineedit.setText(location)
        save_location = '{}/{}'.format(location,filename)
        #except:
            #QMessageBox.warning(self,'Error','you must enter a valid url')
    def handle_locationsaved(self):
        self.log = open('log.txt','w')
        self.locationtosave = self.location.split('/')
        self.locationtosave.remove(self.locationtosave[-1])
        self.locationtosave = '/'.join(self.locationtosave)
        self.log.write(self.locationtosave)
        self.log.close()
    def handle_savedlocation(self):
        self.opening_path = open('log.txt','r')
        self.path = self.opening_path.read()

    def savelocationforvideo(self):
        global startvideo
        global comboboxtext
        global comboboxcontent
        global filetitleforvid
        global urlvideo
        global filepath
        if self.urllineedit_2.text() == '':
            QMessageBox.warning(self,'Error','you must enter a valid url')
        elif self.savelocationlineedit_2.text() == '':
            QMessageBox.warning(self,'Error','use browse button to select valid save location')
        else :
            if self.locationcheck_2.isChecked():
                self.handle_locationsavedforvid()
            filepath = '{}/{}'.format(urlvideo,filetitleforvid)
            comboboxtext = self.comboBox_2.currentText()
            comboboxcontent = [self.comboBox_2.itemText(i) for i in range(self.comboBox_2.count())]
            self.comboBox_2.clear()
            self.urllineedit_2.setText('')
            self.savelocationlineedit_2.setText('')
            self.comboBox_2.clear()
            self.videotitlelineedit.setText('')
            startvideo()
    def handle_browse_forvid(self):
        global save_locationvideo
        try:
            self.locationforvid = QFileDialog.getExistingDirectory(self, caption='Choose location to save your video',
                                                                   directory=self.pathforvid)
            self.savelocationlineedit_2.setText(self.locationforvid)
            save_locationvideo = self.savelocationlineedit_2.text()
        except:
            QMessageBox.warning(self, 'Error', 'you must enter a valid url')

    def handle_locationsavedforvid(self):
        global save_locationvideo
        self.log2 = open('log2.txt', 'w')
        self.log2.write(save_locationvideo)
        self.log2.close()

    def handle_savedlocationforvideo(self):
        self.opening_pathforvid = open('log2.txt', 'r')
        self.pathforvid = self.opening_pathforvid.read()

    def vidcheck(self):
        global st
        global filetitleforvid
        global urlvideo
        try:
            urlvideo = self.urllineedit_2.text()
            self.myvid = pafy.new(urlvideo)
            filetitleforvid = self.myvid.title
            self.videotitlelineedit.setText(filetitleforvid)
            st = self.myvid.allstreams
            for s in st:
                self.size = humanize.naturalsize(s.get_filesize())
                data = '{} {} {} {}'.format(s.mediatype, s.extension, s.quality, self.size)
                self.comboBox_2.addItem(data)
        except:
            pass
    def savelocationforplaylist(self):
        global startplaylist
        global comboboxtextforplaylist
        global comboboxcontent
        if self.urllineedit_7.text() == '':
            QMessageBox.warning(self,'Error','you must enter a valid url')
        elif self.savelocationlineedit_7.text() == '':
            QMessageBox.warning(self,'Error','use browse button to select valid save location')
        elif self.comboBox_5.count() == 0 :
            QMessageBox.warning(self,'Error','you must choose quality to download playlist videos with')
        else:
            if self.locationcheck_7.isChecked():
                self.handle_locationsavedforplaylist()
            comboboxtextforplaylist = self.comboBox_5.currentText()
            self.comboBox_5.clear()
            self.comboBox_6.clear()
            self.urllineedit_7.setText('')
            self.savelocationlineedit_7.setText('')
            self.comboBox_5.clear()
            self.playlisttitlelineedit_4.setText('')
            startplaylist()
    def handle_browse_forplaylist(self):
        global save_locationplaylist
        try:
            self.locationforplaylist = QFileDialog.getExistingDirectory(self,caption='Choose location to save your playlist',directory=self.pathforplaylist)
            self.savelocationlineedit_7.setText(self.locationforplaylist)
            save_locationplaylist = self.savelocationlineedit_7.text()
        except:
            QMessageBox.warning(self, 'Error', 'you must enter a valid url')

    def handle_locationsavedforplaylist(self):
        global save_locationplaylist
        self.log3 = open('log3.txt', 'w')
        self.log3.write(save_locationplaylist)
        self.log3.close()

    def handle_savedlocationforplaylist(self):
        self.opening_pathforplaylist = open('log3.txt', 'r')
        self.pathforplaylist = self.opening_pathforplaylist.read()

    def playlistcheck(self):
        global playliststreams
        global filetitleforplaylist
        global urlplaylist
        global playlist
        global playlistvideos
        global videosofcombobox
        try:
            urlplaylist = self.urllineedit_7.text()
            playlist = pafy.get_playlist(urlplaylist)
            filetitleforplaylist = playlist['title']
            self.playlisttitlelineedit_4.setText(filetitleforplaylist)
            playlistvideos = playlist['items']
            for video in playlistvideos:
                p = video['pafy']
                videotitle = p.title
                self.comboBox_6.addItem(videotitle)
                videosofcombobox.append(videotitle)
        except:
            pass
    def playlistgetselectedvideoquality(self):
        global playlistvideos
        global playlistquality
        global videosofcombobox
        for g in playlistvideos:
            k = g['pafy']
            for d in videosofcombobox:
                if k.title == d :
                    for a in k.allstreams:
                        viddata = '{} {} {}'.format(a.mediatype, a.extension, a.quality)
                        self.comboBox_5.addItem(viddata)
                        playlistquality.append(viddata)
                    break
            break
class pageofdownload(QWidget,FORM_CLASS2):
    global dowloader
    global url
    global save_location
    global filename
    global location
    def __init__(self,parent=None):
        super(pageofdownload,self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.handle_buttons()
        self.urlshow.setText(url)
        self.locationshow.setText(location)
        self.filetitlelineedit.setText(filename)
        self.setFixedSize(511, 260)
    def handle_buttons(self):
        self.cancel_btn.clicked.connect(self.close)
        self.start_btn.clicked.connect(self.download)
    def download(self):
        global dowloader
        global url
        global save_location
        global totalsize
        self.start_btn.setEnabled(False)
        urllib.request.urlretrieve(url,save_location,self.handle_progress_bar)
        QMessageBox.information(self, 'Download Completed', 'Your download successfully downloaded')
        self.lineEdit_2.setText('{} MB'.format(str(self.totalsizeforglobal)))
        self.lineEdit_3.setText('0.0 MB')
        QApplication.processEvents()
        self.start_btn.setEnabled(True)
    def handle_progress_bar(self ,blocknum,blocksize,totalsize):
        global count
        read = blocknum * blocksize
        self.read = round(Decimal(blocknum * blocksize * 0.000001),1)
        self.totalsize = round(Decimal(totalsize * 0.000001),1)
        self.totalsizeforglobal = self.totalsize
        if blocknum == 0:
            self.start_time = time.time()
            return
        if count < 4 :
            count += 1
        else :
            self.duration = time.time() - self.start_time
            self.progress_size = int(blocknum * blocksize)
            self.speed = int(self.progress_size / (1024 * self.duration))
            self.lineEdit_4.setText('{} KB/sec'.format(self.speed))
            QApplication.processEvents()
            self.timeremain = int(int(totalsize - read) / (self.speed / 0.001))
            print(self.timeremain)
            '''
            self.sec = timedelta(seconds=int(self.timeremain))
            self.t = datetime(4, 4, 4) + self.sec
            self.etaedited = '{}h {}min {}sec'.format(self.t.hour, self.t.minute, self.t.second)
            self.lineEdit_5.setText(self.etaedited)
            QApplication.processEvents()
            '''
        self.lineEdit_2.setText('{} MB'.format(str(self.read)))
        QApplication.processEvents()
        self.lineEdit_3.setText('{} MB'.format(str(self.totalsize-self.read)))
        QApplication.processEvents()
        self.progressBar.setValue(int(read* 100 / totalsize))
        QApplication.processEvents()

class pageofvideodownload(QWidget,FORM_CLASS3):
    def __init__(self,parent=None):
        global dowloader
        global urlvideo
        global save_locationvideo
        global filetitleforvid
        global st
        global comboboxtext
        global videosize
        super(pageofvideodownload,self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.fillcombo()
        self.setFixedSize(511,327)
        self.handle_buttons()
        self.urlshow.setText(urlvideo)
        self.locationshow.setText(save_locationvideo)
        self.videotitlelineedit.setText(filetitleforvid)
        self.lineEdit.setText(' '.join(comboboxtext.split()[-2:]))
        videosize = float(' '.join(comboboxtext.split()[-2:-1]))
        self.lineEdit_2.setText('0.0 MB')
        self.lineEdit_3.setText(self.lineEdit.text())
    def videostartdownload(self):
        global save_locationvideo
        self.start_btn.setEnabled(False)
        downloadvideo = st[self.selectedquality.currentIndex()].download(filepath=save_locationvideo,callback =self.download_progress)
        self.lineEdit_2.setText('{} MB'.format(str(float(videosize))))
        self.lineEdit_3.setText('0.0 MB')
        self.progressBar.setValue(100)
        QMessageBox.information(self, 'Download Completed', 'Your download successfully downloaded')
    def handle_buttons(self):
        self.cancel_btn.clicked.connect(self.close)
        self.start_btn.clicked.connect(self.videostartdownload)
    def fillcombo(self):
        global comboboxtext
        global comboboxcontent
        global videosize
        for p in comboboxcontent:
            self.selectedquality.addItem(p)
        comboboxindexforvideo= self.selectedquality.findText(comboboxtext)
        self.selectedquality.setCurrentIndex(comboboxindexforvideo)
    def download_progress(self,total, recvd, ratio, rate, eta):
        global filepath
        global videosize
        videoprogresssize = round(Decimal(recvd * 0.000001),1)
        self.lineEdit_2.setText('{} MB'.format(videoprogresssize))
        QApplication.processEvents()
        self.lineEdit_3.setText('{} MB'.format(round(Decimal(Decimal(videosize)-videoprogresssize),1)))
        QApplication.processEvents()
        downloadratio = int(''.join(list(str(ratio))[2:4]))
        if float(''.join(list(str(ratio))[:2])) == 1.0 :
            downloadration = 100
        self.progressBar.setValue(downloadratio)
        QApplication.processEvents()
        self.lineEdit_4.setText('{} KB/sec'.format(int(rate)))
        QApplication.processEvents()
        sec = timedelta(seconds=int(eta))
        t = datetime(1, 1, 1) + sec
        etaedited = '{}h {}min {}sec'.format(t.hour, t.minute, t.second)
        self.lineEdit_5.setText(etaedited)
        QApplication.processEvents()
class pageofplaylistdownload(QWidget,FORM_CLASS4):
    def __init__(self,parent=None):
        global filetitleforplaylist
        global urlplaylist
        global save_locationplaylist
        super(pageofplaylistdownload,self).__init__(parent)
        self.setupUi(self)
        self.handle_buttons()
        self.fillcombo()
        self.setFixedSize(511,361)
        self.videosofcombobox = len(videosofcombobox)
        self.lcdNumber_2.display(len(videosofcombobox))
        videosofcombobox.clear()
        self.urlshow.setText(urlplaylist)
        self.locationshow.setText(save_locationplaylist)
        self.playlisttitlelineedit.setText(filetitleforplaylist)
    def playliststartdownload(self):
        global save_locationplaylist
        global filetitleforplaylist
        self.downloadingvideonumber = 1
        self.downloadedvideos = 0
        self.start_btn.setEnabled(False)
        os.chdir(save_locationplaylist)
        if os.path.exists(filetitleforplaylist):
            os.chdir(filetitleforplaylist)
        else:
            os.mkdir(filetitleforplaylist)
            os.chdir(filetitleforplaylist)
        for g in playlistvideos:
            try :
                k = g['pafy']
                f = k.allstreams
                self.lcdNumber.display(self.downloadingvideonumber)
                QApplication.processEvents()
                startdownloading = f[self.selectedquality.currentIndex()].download(callback=self.download_progress)
                self.downloadedvideos += 1
                self.lcdNumber_3.display(self.downloadedvideos)
                QApplication.processEvents()
                self.videosofcombobox -= 1
                self.lcdNumber_2.display(self.videosofcombobox)
                QApplication.processEvents()
                self.downloadingvideonumber += 1
            except :
                self.downloadedvideos += 1
                self.lcdNumber_3.display(self.downloadedvideos)
                QApplication.processEvents()
                self.videosofcombobox -= 1
                self.lcdNumber_2.display(self.videosofcombobox)
                QApplication.processEvents()
                self.downloadingvideonumber += 1
        self.lcdNumber.display(0)
        self.lcdNumber_2.display(0)
        self.progressBar.setValue(100)
        self.lineEdit_3.setText('0.0 MB')
        QMessageBox.information(self, 'Download Completed', 'Your playlist successfully downloaded')
    def handle_buttons(self):
        self.cancel_btn.clicked.connect(self.close)
        self.start_btn.clicked.connect(self.playliststartdownload)
    def fillcombo(self):
        global playlistquality
        global comboboxtextforplaylist
        for p in playlistquality:
            self.selectedquality.addItem(p)
        comboboxindexforplaylist = self.selectedquality.findText(comboboxtextforplaylist)
        self.selectedquality.setCurrentIndex(comboboxindexforplaylist)
    def download_progress(self,total, recvd, ratio, rate, eta):
        self.videoforplaylistprogresssize = round(Decimal(recvd * 0.000001),1)
        self.lineEdit_2.setText('{} MB'.format(self.videoforplaylistprogresssize))
        QApplication.processEvents()
        self.lineEdit_3.setText('{} MB'.format(round(Decimal(Decimal(total * 0.000001)-self.videoforplaylistprogresssize),1)))
        QApplication.processEvents()
        self.downloadratio = int(''.join(list(str(ratio))[2:4]))
        if float(''.join(list(str(ratio))[:2])) == 1.0 :
            downloadration = 100
        self.progressBar.setValue(self.downloadratio)
        QApplication.processEvents()
        self.lineEdit_4.setText('{} KB/sec'.format(int(rate)))
        QApplication.processEvents()
        self.sec = timedelta(seconds=int(eta))
        self.t = datetime(1, 1, 1) + self.sec
        self.etaedited = '{}h {}min {}sec'.format(self.t.hour, self.t.minute, self.t.second)
        self.lineEdit_5.setText(self.etaedited)
        QApplication.processEvents()
listofdownloadwindows = []
counter = 0
listofdownloadvideowindows = []
counter2 = 0
listofdownloadplaylistwindows = []
counter3 = 0
playlistquality = []
videosofcombobox = []
count = 0
app = QApplication(sys.argv)
window = dowloader()
window.show()
app.exec_()
