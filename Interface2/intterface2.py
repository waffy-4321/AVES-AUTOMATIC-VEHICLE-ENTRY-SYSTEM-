import numpy as np
import cv2
import imutils
from PyQt5 import QtCore, QtGui, QtWidgets
from intterface3 import *

class Ui_Interface2(object):
    def process(self):
        image = cv2.imread('c:/img8.png')
        image = imutils.resize(image, width=500)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray, 11, 65,65)
        edged = cv2.Canny(gray, 30, 200)
        cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        img2 = image.copy()
        cv2.drawContours(img2, cnts, -1, (0,255,0), 3)
        cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
        NumberPlateCnt = None
        license_plate = None
        x = None
        y = None
        w = None
        h = None
        img3 = image.copy()
        cv2.drawContours(img3, cnts, -1, (0,255,0), 3)
        idx=1
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            # print ("approx = ",approx)
            if len(approx) == 4:
                NumberPlateCnt = approx
                x, y, w, h = cv2.boundingRect(c)
                license_plate = image[y:y + h, x:x + w]
                cv2.imwrite('C:/Users/Sumit Khohal/Desktop/Cropped image/' + str(idx) + '.png', license_plate)
                idx+=1
                break
        cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0),3)
        image = cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 3)
        i=1
        Cropped_img = 'C:/Users/Sumit Khohal/Desktop/Cropped image/'+ str(i) +'.png'
        i+=1
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_interface3()
        self.ui.setupUi(self.window)
        self.window.show() 

    def processtwo(self):
        image = cv2.imread('c:/img8.png')
        image = imutils.resize(image, width=500)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray,9,75,75)
        edged = cv2.Canny(gray, 30, 200)
        cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        img2 = image.copy()
        cv2.drawContours(img2, cnts, -1, (0,255,0), 3)

        cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
        NumberPlateCnt = None
        license_plate = None
        x = None
        y = None
        w = None
        h = None
        img3 = image.copy()
        cv2.drawContours(img3, cnts, -1, (0,255,0), 3)
        idx=1
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            # print ("approx = ",approx)
            if len(approx) == 4:
                NumberPlateCnt = approx
                
                x, y, w, h = cv2.boundingRect(c)
                license_plate = image[y:y + h, x:x + w]
                cv2.imwrite('C:/Users/Sumit Khohal/Desktop/Cropped image/' + str(idx) + '.png', license_plate)
                idx+=1
                
                break

        cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0),3)
        image = cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 3)

        i=1
        Cropped_img = 'C:/Users/Sumit Khohal/Desktop/Cropped image/'+ str(i) +'.png'
        i+=1
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_interface3()
        self.ui.setupUi(self.window)
        self.window.show()
    def processthree(self):
        image = cv2.imread('c:/img12.png')

        image = imutils.resize(image, width=500)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray = cv2.bilateralFilter(gray, 12, 75,75)

        edged = cv2.Canny(gray, 30, 200)
       

        cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        img2 = image.copy()
        cv2.drawContours(img2, cnts, -1, (0,255,0), 3)

        cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
        NumberPlateCnt = None
        license_plate = None
        x = None
        y = None
        w = None
        h = None
        img3 = image.copy()
        cv2.drawContours(img3, cnts, -1, (0,255,0), 3)
        idx=1
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            # print ("approx = ",approx)
            if len(approx) == 4:
                NumberPlateCnt = approx
                
                x, y, w, h = cv2.boundingRect(c)
                license_plate = image[y:y + h, x:x + w]
                cv2.imwrite('C:/Users/Sumit Khohal/Desktop/Cropped image/' + str(idx) + '.png', license_plate)
                idx+=1
                
                break

        cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0),3)
        image = cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 3)

        i=1
        Cropped_img = 'C:/Users/Sumit Khohal/Desktop/Cropped image/'+ str(i) +'.png'
        i+=1
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_interface3()
        self.ui.setupUi(self.window)
        self.window.show() 
   
    def setupUi(self, Interface2):
        Interface2.setObjectName("Interface2")
        Interface2.resize(772, 733)
        Interface2.setStyleSheet("background-image: url(:/images/111.jpeg);")
        self.centralwidget = QtWidgets.QWidget(Interface2)
        self.centralwidget.setObjectName("centralwidget")
        self.Process1 = QtWidgets.QPushButton(self.centralwidget)
      
        self.Process1.setGeometry(QtCore.QRect(50, 590, 191, 81))
        self.Process1.setStyleSheet("border-image: url(:/images/PROCESS 1.png);")
        self.Process1.setText("")
       
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/process1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Process1.setIcon(icon)
        self.Process1.setIconSize(QtCore.QSize(200, 110))
        self.Process1.setObjectName("Process1")
        self.Process1.clicked.connect(self.process)
        self.Process2 = QtWidgets.QPushButton(self.centralwidget)
        self.Process2.setGeometry(QtCore.QRect(290, 590, 191, 81))
        self.Process2.setStyleSheet("border-image: url(:/images/PROCESS 2.png);")
        self.Process2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/process2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Process2.setIcon(icon1)
        self.Process2.setIconSize(QtCore.QSize(175, 125))
        self.Process2.setObjectName("Process2")
        self.Process2.clicked.connect(self.processtwo)
        self.Process3 = QtWidgets.QPushButton(self.centralwidget)
        self.Process3.setGeometry(QtCore.QRect(530, 590, 191, 81))
        self.Process3.setStyleSheet("border-image: url(:/images/PROCESS 3.png);")
        self.Process3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/process3.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Process3.setIcon(icon2)
        self.Process3.setIconSize(QtCore.QSize(200, 100))
        self.Process3.setObjectName("Process3")
        self.Process3.clicked.connect(self.processthree)
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(50, 120, 651, 411))
        self.Image.setText("")
        self.Image.setPixmap(QtGui.QPixmap("c:/img8.png"))  #here we will add the path of the image
        self.Image.setScaledContents(True)
        self.Image.setObjectName("Image")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 20, 351, 81))
        self.label.setStyleSheet("\n""border-image: url(:/images/downloa1d.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        Interface2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Interface2)
        self.statusbar.setObjectName("statusbar")
        Interface2.setStatusBar(self.statusbar)

        self.retranslateUi(Interface2)
        QtCore.QMetaObject.connectSlotsByName(Interface2)

    def retranslateUi(self, Interface2):
        _translate = QtCore.QCoreApplication.translate
        Interface2.setWindowTitle(_translate("Preprocessing", "Preprocessing"))
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Interface2 = QtWidgets.QMainWindow()
    ui = Ui_Interface2()
    ui.setupUi(Interface2)
    Interface2.show()
    sys.exit(app.exec_())
