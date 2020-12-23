from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_interface5(object):
    def setupUi(self, interface5):
        interface5.setObjectName("interface5")
        interface5.resize(772, 733)
        interface5.setStyleSheet("border-image: url(:/images/111.jpeg);")
        self.centralwidget = QtWidgets.QWidget(interface5)
        self.centralwidget.setObjectName("centralwidget")
        self.Sub = QtWidgets.QPushButton(self.centralwidget)
        self.Sub.setGeometry(QtCore.QRect(190, 270, 401, 321))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Sub.setFont(font)
        self.Sub.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Sub.setAutoFillBackground(False)
        self.Sub.setStyleSheet("border-image: url(:/images/access granted.jpg);")
        self.Sub.setText("")
        self.Sub.setObjectName("Sub")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(230, 40, 311, 71))
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
        interface5.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(interface5)
        self.statusbar.setObjectName("statusbar")
        interface5.setStatusBar(self.statusbar)

        self.retranslateUi(interface5)
        QtCore.QMetaObject.connectSlotsByName(interface5)

    def retranslateUi(self, interface5):
        _translate = QtCore.QCoreApplication.translate
        interface5.setWindowTitle(_translate("Access granted", "Access Granted"))
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    interface5 = QtWidgets.QMainWindow()
    ui = Ui_interface5()
    ui.setupUi(interface5)
    interface5.show()
    sys.exit(app.exec_())
