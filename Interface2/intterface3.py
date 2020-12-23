import numpy as np
import cv2
import imutils
import mysql.connector
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
from PyQt5 import QtCore, QtGui, QtWidgets
from intterface2 import *
from intterface4 import *
from intterface5 import *
from datetime import datetime

class Ui_interface3(object):
     
    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Interface2()
        self.ui.setupUi(self.window)
        self.window.show()
    def ocr(self):
        i=1
        Cropped_img = 'C:/Users/Sumit Khohal/Desktop/Cropped image/'+ str(i) +'.png'
        i+=1
        plate = cv2.cvtColor(cv2.imread(Cropped_img), cv2.COLOR_BGR2GRAY)

        plate1= cv2.bilateralFilter(plate,11,35,35)
        config = ('-l eng --oem 1 --psm 3')
        text = pytesseract.image_to_string(plate1, config=config)
        #print('NUMBER IS :', text)
        j=1
        f=open('C:/Users/Sumit Khohal/Desktop/Cropped image/'+ str(j) +'.txt','w')
        f.write(text)
        f.close()
        j+=1
        f=open('C:/Users/Sumit Khohal/Desktop/Cropped image/1.txt','r')
        data = f.read()
        self.textEdit.setText(data)
        f.close()
    
    def update1(self):
        f=open('C:/Users/Sumit Khohal/Desktop/Cropped image/1.txt','r+')
        f.seek(0)
        f.truncate()
        textvalue=self.textEdit.toPlainText()
        f.write(textvalue)
        f.close()

    def CHECK(self):
        try:
            connection = mysql.connector.connect(host='localhost',database='AVES',user='root',password='root')
            cursor = connection.cursor()
            textvalue=self.textEdit.toPlainText()
            if(connection.is_connected()):
                print("MySql Connection is established")
                #val = cursor.fetchall()
                query = """SELECT NUMBERPLATE FROM MASTERTABLE WHERE NUMBERPLATE= %s"""
                cursor.execute(query,(textvalue,))
                record=cursor.fetchone()
                if(record == None):
                    rec = record
                else:
                    rec = record[0]
                print(rec)
                if(rec == textvalue):
                    now = datetime.now()
                    numberplate = self.textEdit.toPlainText()
                    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
                    #print(formatted_date)
                    query1 =cursor.execute( """SELECT COUNT(ARRIVAL) FROM TRANSACTIONTABLE WHERE NUMBERPLATE= %s""",(textvalue,))
                    record1=cursor.fetchone()
                    print(record1)
                    query2 =cursor.execute( """SELECT COUNT(DEPARTURE) FROM TRANSACTIONTABLE WHERE NUMBERPLATE= %s""",(textvalue,))
                    record2=cursor.fetchone()
                    print(record2)
                    #print(query1)
                    #print(query2)
                    if(record1==record2):
                        print("hello1")
                        cursor.execute("""insert into TRANSACTIONTABLE(NUMBERPLATE, ARRIVAL) values(%s,%s)""", (textvalue,formatted_date))
                        connection.commit()

                    else:
                        cursor.execute("""update TRANSACTIONTABLE SET DEPARTURE =%s WHERE NUMBERPLATE = %s""", (formatted_date, textvalue))
                        connection.commit()
                    self.window=QtWidgets.QMainWindow()
                    self.ui=Ui_interface5()
                    self.ui.setupUi(self.window)
                    self.window.show()
                    
                    
                else:
                    self.window=QtWidgets.QMainWindow()
                    self.ui=Ui_interface4()
                    self.ui.setupUi(self.window)
                    self.window.show() 
        except:
            print("ERROR")
        finally:          
                cursor.close()
                connection.close()
                print("MySQL connection is closed")  

    def setupUi(self, interface3):
        interface3.setObjectName("interface3")
        interface3.resize(772, 733)
        interface3.setStyleSheet("background-image: url(:/images/111.jpeg);")
        self.centralwidget = QtWidgets.QWidget(interface3)
        self.centralwidget.setObjectName("centralwidget")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(50, 540, 91, 81))
        self.Button1.setStyleSheet("border-image: url(:/images/ocr.png);")
        self.Button1.setText("")
        self.Button1.setObjectName("Button1")
        self.Button1.clicked.connect(self.ocr)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(250, 20, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setStyleSheet("border-image: url(:/images/downloa1d.png);")
        self.label1.setText("")
        self.label1.setScaledContents(False)
        self.label1.setObjectName("label1")
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(320, 460, 131, 81))
        self.Button2.setStyleSheet("border-image: url(:/images/back1.png);")
        self.Button2.setText("")
        self.Button2.setObjectName("Button2")
        self.Button2.clicked.connect(self.back)
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(580, 540, 141, 81))
        self.Button3.setStyleSheet("border-image: url(:/images/check.png);")
        self.Button3.setText("")
        self.Button3.setIconSize(QtCore.QSize(30, 30))
        self.Button3.setObjectName("Button3")
        self.Button3.clicked.connect(self.CHECK)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(60, 150, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setStyleSheet("border-image: url(:/images/numberplate.PNG);")
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(60, 290, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setStyleSheet("border-image: url(:/images/text.png);")
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.number = QtWidgets.QLabel(self.centralwidget)
        self.number.setGeometry(QtCore.QRect(410, 140, 321, 81))
        self.number.setText("")
        self.number.setPixmap(QtGui.QPixmap('C:/Users/Sumit Khohal/Desktop/Cropped image/1.png'))
        self.number.setScaledContents(True)
        self.number.setObjectName("number")
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(390, 280, 341, 71))
        self.textEdit.setStyleSheet("border-image: url(:/images/blank.jpg);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFont(font)
        self.update = QtWidgets.QPushButton(self.centralwidget)
        self.update.setGeometry(QtCore.QRect(500, 370, 141, 51))
        self.update.setStyleSheet("border-image: url(:/images/update.png);")
        self.update.setText("")
        self.update.setIconSize(QtCore.QSize(200, 250))
        self.update.setObjectName("update")
        self.update.clicked.connect(self.update1)
        interface3.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(interface3)
        self.statusbar.setObjectName("statusbar")
        interface3.setStatusBar(self.statusbar)

        self.retranslateUi(interface3)
        QtCore.QMetaObject.connectSlotsByName(interface3)

    def retranslateUi(self, interface3):
        _translate = QtCore.QCoreApplication.translate
        interface3.setWindowTitle(_translate("OCR", "OCR"))

import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    interface3 = QtWidgets.QMainWindow()
    ui = Ui_interface3()
    ui.setupUi(interface3)
    interface3.show()
    sys.exit(app.exec_())
