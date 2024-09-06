# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(412, 516)
        font = QtGui.QFont()
        font.setPointSize(27)
        Login.setFont(font)
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(60, 30, 371, 441))
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 20, 300, 420))
        self.label.setStyleSheet("border-image: url(:/newPrefix/14546211_rm127-tang-16b-japaneseframe.jpg);\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 40, 280, 390))
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0, 0.4);  /* 40% opacity */\n"
"border-radius: 15px;\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 110, 301, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(255,255,255,0);\n"
"color : rgba(255,255,255,210)")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(79, 150, 201, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"border : none;\n"
"border-bottom : 3px solid rgba(243, 243, 243,0.8);\n"
"color : rgba(255,255,255,1);\n"
"padding-bottom : 7px;\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 220, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"border : none;\n"
"border-bottom : 3px solid rgba(243, 243, 243,0.8);\n"
"color : rgba(255,255,255,1);\n"
"padding-bottom : 7px;\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 310, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton#pushButton {\n"
"    color: rgba(0, 0, 0, 0.7);\n"
"    border: none;  /* Memperbaiki kesalahan pengetikan \"boder\" menjadi \"border\" */\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0.477, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0.2), stop:1 rgba(255, 255, 255, 0.9));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(105, 118, 132, 1);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 300, 421))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.438, y1:0, x2:0.494, y2:1, stop:0 rgba(0, 0, 0, 0.2), stop:1 rgba(255, 255, 255, 0.7));\n"
"border-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(80, 350, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color : rgba(255,255,255,0.7);")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(209, 350, 68, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"color : rgba(255,255,255,0.7);\n"
"background-color: rgba(255, 255, 255,0);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover{\n"
"border: none;\n"
"border-bottom: 0.5px solid rgba(255,255,255,1);\n"
"}\n"
"")
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 380, 35, 35))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(25)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
"color : rgba(200,200,200,1);\n"
"background-color : rgba(255,255,255,0);\n"
"}\n"
"\n"
"QPushButton#pushButton_3:hover{\n"
"color:rgba(240,240,240,1);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 380, 35, 35))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(25)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
"color : rgba(200,200,200,1);\n"
"background-color : rgba(255,255,255,0);\n"
"}\n"
"\n"
"QPushButton#pushButton_4:hover{\n"
"color:rgba(240,240,240,1);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 380, 35, 35))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(25)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton#pushButton_5{\n"
"color : rgba(200,200,200,1);\n"
"background-color : rgba(255,255,255,0);\n"
"}\n"
"\n"
"QPushButton#pushButton_5:hover{\n"
"color:rgba(240,240,240,1);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 380, 35, 35))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(25)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton#pushButton_6{\n"
"color : rgba(200,200,200,1);\n"
"background-color : rgba(255,255,255,0);\n"
"}\n"
"\n"
"QPushButton#pushButton_6:hover{\n"
"color:rgba(240,240,240,1);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 50, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Modern")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("QPushButton#pushButton_7{\n"
"background-color : rgba(0,0,0,0);\n"
"color :rgba(255,255,255,0.8);\n"
"}\n"
"QPushButton#pushButton_7:hover{\n"
"color:rgba(255, 0, 0,0.6);\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.error = QtWidgets.QLabel(self.frame)
        self.error.setGeometry(QtCore.QRect(80, 280, 201, 16))
        self.error.setStyleSheet("color :rgb(207, 187, 188);\n"
"background-color : rgba(0,0,0,0);")
        self.error.setText("")
        self.error.setObjectName("error")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.label_5.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.error.raise_()

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.label_4.setText(_translate("Login", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Login", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Login", "Password"))
        self.pushButton.setText(_translate("Login", "L o g   I n"))
        self.label_5.setText(_translate("Login", "<html><head/><body><p>Don\'t have an account yet?</p></body></html>"))
        self.pushButton_2.setText(_translate("Login", "Create One"))
        self.pushButton_3.setText(_translate("Login", "H"))
        self.pushButton_4.setText(_translate("Login", "L"))
        self.pushButton_5.setText(_translate("Login", "M"))
        self.pushButton_6.setText(_translate("Login", "Y"))
        self.pushButton_7.setText(_translate("Login", "X"))
import Resources_Login_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())