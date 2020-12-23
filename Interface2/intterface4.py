import mysql.connector
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from intterface5 import *
from datetime import datetime

class Ui_interface4(object):

    def submit1(self):
            try:
                ownername=self.TE1.toPlainText()
                numberplate =self.TE2.toPlainText()
                
                connection =mysql.connector.connect(host='localhost',database='AVES',user='root',password='root')
                cur =connection.cursor(prepared = True)
                print("Connection established")
                query = """INSERT INTO MASTERTABLE(NUMBERPLATE, OWNERNAME) VALUES (%s,%s)"""
                cur.execute(query,(numberplate, ownername))
                connection.commit()
                msg=QMessageBox()
                msg.setText("Data Entered!")
                x=msg.exec_()
                
                
            except:
                msg=QMessageBox()
                msg.setText("Data not Entered!")
                x=msg.exec_()
            finally:
                    cur.close()
                    connection.close()
                    print("connection closed")
           
    def aves(self):
        try:
            connection = mysql.connector.connect(host='localhost',database='AVES',user='root',password='root')
            cursor = connection.cursor()
            textvalue=self.TE2.toPlainText()
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
                    numberplate = self.TE2.toPlainText()
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
        except:
            print("ERROR")
        finally:          
                cursor.close()
                connection.close()
                print("MySQL connection is closed")  
    def setupUi(self, interface4):
        interface4.setObjectName("interface4")
        interface4.resize(772, 733)
        interface4.setStyleSheet("border-image: url(:/images/111.jpeg);")
        self.centralwidget = QtWidgets.QWidget(interface4)
        self.centralwidget.setObjectName("centralwidget")
        self.Sub = QtWidgets.QPushButton(self.centralwidget)
        self.Sub.setGeometry(QtCore.QRect(110, 550, 171, 71))
        self.Sub.setStyleSheet("\n""border-image: url(:/images/submit11.png);")
        self.Sub.setText("")
        self.Sub.setObjectName("Sub")
        self.Sub.clicked.connect(self.submit1)
        interface4.setCentralWidget(self.centralwidget)  




        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(240, 20, 311, 71))
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
        self.Check = QtWidgets.QPushButton(self.centralwidget)
        self.Check.setGeometry(QtCore.QRect(470, 550, 181, 61))
        self.Check.setStyleSheet("border-image: url(:/images/check1.jpg);")
        self.Check.setText("")
        self.Check.setObjectName("Check")
        self.Check.clicked.connect(self.aves)

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(60, 160, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setStyleSheet("border-image: url(:/images/OWNER NAME.PNG);")
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(60, 310, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setStyleSheet("border-image: url(:/images/text.png);")
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.TE2 = QtWidgets.QTextEdit(self.centralwidget)
        self.TE2.setEnabled(True)
        self.TE2.setGeometry(QtCore.QRect(450, 310, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TE2.setFont(font)
        self.TE2.setStyleSheet("border-image: url(:/images/blank.jpg);")
        self.TE2.setObjectName("TE2")
        f=open('C:/Users/Sumit Khohal/Desktop/Cropped image/1.txt','r')
        data = f.read()
        self.TE2.setText(data)
        f.close()
        self.TE1 = QtWidgets.QTextEdit(self.centralwidget)
        self.TE1.setEnabled(True)
        self.TE1.setGeometry(QtCore.QRect(450, 160, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.TE1.setFont(font)
        self.TE1.setStyleSheet("border-image: url(:/images/blank.jpg);")
        self.TE1.setObjectName("TE1")
        
        interface4.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(interface4)
        self.statusbar.setObjectName("statusbar")
        interface4.setStatusBar(self.statusbar)

        self.retranslateUi(interface4)
        QtCore.QMetaObject.connectSlotsByName(interface4)

        

    def retranslateUi(self, interface4):
        _translate = QtCore.QCoreApplication.translate
        interface4.setWindowTitle(_translate("New User", "New User"))
        self.Sub.setText(_translate("interface4",""))


import icons
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    interface4 = QtWidgets.QMainWindow()
    ui = Ui_interface4()
    ui.setupUi(interface4)
    interface4.show()
    sys.exit(app.exec_())
