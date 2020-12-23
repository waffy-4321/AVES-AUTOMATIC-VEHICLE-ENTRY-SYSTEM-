from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap 
from PyQt5.QtWidgets import  QApplication
from PyQt5.uic import loadUi
from intterface2 import *
import matplotlib.pyplot as plt

#from idlelib import window
class Ui_interface1(object):
    
    
    def setupUi(self, interface1):
        interface1.setObjectName("interface1")
        interface1.setWindowModality(QtCore.Qt.NonModal)
        interface1.resize(772, 733)
        interface1.setAutoFillBackground(False)
        interface1.setStyleSheet("border-image: url(:/images/111.jpeg);")
        self.label1 = QtWidgets.QLabel(interface1)
        self.label1.setGeometry(QtCore.QRect(240, 10, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setStyleSheet("border-image: url(:/images/downloa1d.png);")
        self.label1.setText("")
        self.label1.setScaledContents(False)
        self.label1.setObjectName("label1")
        self.SHOW = QtWidgets.QPushButton(interface1)
        self.SHOW.setGeometry(QtCore.QRect(70, 570, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.SHOW.setFont(font)
        self.SHOW.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/open-camera.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SHOW.setIcon(icon)
        self.SHOW.setIconSize(QtCore.QSize(350, 300))
        self.SHOW.setObjectName("SHOW")
        self.imgLabel = QtWidgets.QLabel(interface1)
        self.imgLabel.setGeometry(QtCore.QRect(60, 100, 651, 321))
        self.imgLabel.setAcceptDrops(False)
        self.imgLabel.setAutoFillBackground(False)
        self.imgLabel.setStyleSheet("")
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imgLabel.setLineWidth(4)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.CAPTURE = QtWidgets.QPushButton(interface1)
        self.CAPTURE.setGeometry(QtCore.QRect(330, 570, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.CAPTURE.setFont(font)
        self.CAPTURE.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/capture.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CAPTURE.setIcon(icon1)
        self.CAPTURE.setIconSize(QtCore.QSize(150, 150))
        self.CAPTURE.setObjectName("CAPTURE")
        self.CLOSE = QtWidgets.QPushButton(interface1)
        self.CLOSE.setGeometry(QtCore.QRect(580, 570, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.CLOSE.setFont(font)
        self.CLOSE.setStyleSheet("")
        self.CLOSE.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/computer-icons-arrow-button-next-step-png-clip-art.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CLOSE.setIcon(icon2)
        self.CLOSE.setIconSize(QtCore.QSize(125, 100))
        self.CLOSE.setObjectName("CLOSE")
        self.CLOSE.clicked.connect(self.close)

        self.retranslateUi(interface1)
        QtCore.QMetaObject.connectSlotsByName(interface1)
        self.SHOW.clicked.connect(self.onClicked)
        self.logic = 0
        self.SHOW.clicked.connect(self.onClicked)
        self.CAPTURE.clicked.connect(self.CaptureClicked)
        #self.CLOSE.clicked.connect(QtWidgets.qApp.quit)
    def onClicked(self):
        cap = cv2.VideoCapture(0)
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                self.displayImage(frame, 1)
                cv2.waitKey()

                if (self.logic==1):
                    cv2.imwrite('Images/1.png', frame)
                    self.logic = 1
                    cap.release()
                    cv2.destroyAllWindows()
            else :
                print('return not found')
        

    def CaptureClicked(self): 
        self.logic = 1
    
    def close(self):
        
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Interface2()
        self.ui.setupUi(self.window)
        self.window.show()
    def displayImage(self, img,window=1):
        qformat = QImage.Format_Indexed8

        if len(img.shape) == 3:
                if (img.shape[2]) == 4:
                    qformat = QImage.Format_RGBA888
                else:
                    qformat = QImage.Format_RGB888
                    img = QImage(img, img.shape[1], img.shape[0], qformat)
                    img = img.rgbSwapped()
                    self.imgLabel.setPixmap(QPixmap.fromImage(img))
                    self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def retranslateUi(self, interface1):
        _translate = QtCore.QCoreApplication.translate
        interface1.setWindowTitle(_translate("Capture image", "Capture image"))

import icons

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    interface1 = QtWidgets.QMainWindow()
    ui = Ui_interface1()
    ui.setupUi(interface1)
    interface1.show()
    sys.exit(app.exec_())
