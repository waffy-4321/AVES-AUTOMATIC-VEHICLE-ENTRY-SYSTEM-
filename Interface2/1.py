from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap 
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from interface2 import Ui_Interface2
import matplotlib.pyplot as plt
#from idlelib import window
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(772, 733)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("border-image: url(:/images/111.jpeg);")
        self.label1 = QtWidgets.QLabel(Dialog)
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
        self.SHOW = QtWidgets.QPushButton(Dialog)
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
        self.imgLabel = QtWidgets.QLabel(Dialog)
        self.imgLabel.setGeometry(QtCore.QRect(60, 100, 651, 321))
        self.imgLabel.setAcceptDrops(False)
        self.imgLabel.setAutoFillBackground(False)
        self.imgLabel.setStyleSheet("")
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imgLabel.setLineWidth(4)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.CAPTURE = QtWidgets.QPushButton(Dialog)
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
        self.CLOSE = QtWidgets.QPushButton(Dialog)
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.SHOW.clicked.connect(self.onClicked)
        self.logic = 0
        self.value = 1
        self.SHOW.clicked.connect(self.onClicked)
        self.CAPTURE.clicked.connect(self.CaptureClicked)
        self.CLOSE.clicked.connect(self.OffClicked)
    def onClicked(self):
        

        cap= cv2.VideoCapture(0)

        if cap.isOpened():
            ret, frame = cap.read()
            print(ret)
            print(frame)
            
        else:
                ret = False
        
        
        while (cap.isOpened()):

            ret, frame = cap.read()
            if ret == True:
                self.displayImage(frame, 1)
                cv2.waitKey()

                if (self.logic==2):
                    self.value = self.value+1
                    cv2.imwrite('Images/%s.png'%(self.value), frame)
                    self.logic = 1
            else :
                print('return not found')
        cap.release()
        cv2.destroyAllWindows()
    def CaptureClicked(self): 
        self.logic = 2
        cv2.waitKey(0)
    def OffClicked(self):
        self.Interface2 = QtWidgets.QMainWindow()
        self.ui = Ui_Interface2()
        self.ui.setupUi(self.Interface2)
        self.Interface2.show()
        cap.close()
       # window.close()

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
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

import icons

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
