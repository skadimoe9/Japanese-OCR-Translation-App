import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QWidget


# --> Splash Screen
from Splash_Screen import Ui_SplashScreen
from Login import Ui_Login
from Register import Ui_Register
from Social import Ui_Social

# --> Global
counter = 0

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()  # Membuat instance dari kelas Ui_SplashScreen
        self.ui.setupUi(self)  # Menginisialisasi UI
        
        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Drop Shadow Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setOffset(0, 0)  # Set offset for both X and Y
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)  # Applying shadow effect to the frame

        # QTimer ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        
        self.show()  # Menampilkan jendela splash screen

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()
            self.main = Login()  # Mengalihkan ke jendela Login
            self.main.show()
            self.close()

        counter += 4

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()  # Gunakan Ui_Login, bukan Ui_Form
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.adjustSize()
        
        
        # Menghubungkan tombol X (pushButton_7) ke metode close()
        self.ui.pushButton_7.clicked.connect(self.close)

        # Menghubungkan tombol "Create One" ke metode openRegister
        self.ui.pushButton_2.clicked.connect(self.openRegister)

        # Menghubungkan tombol ke metode openSocial
        self.ui.pushButton_3.clicked.connect(self.openSocial)
        self.ui.pushButton_4.clicked.connect(self.openSocial)
        self.ui.pushButton_5.clicked.connect(self.openSocial)
        self.ui.pushButton_6.clicked.connect(self.openSocial)

    def openRegister(self):
        print("Opening Register Window")  # Debugging Statement
        self.registerWindow = Register()  # Menginisialisasi kelas Register
        self.registerWindow.show()
        self.close()

    def openSocial(self):
        print("Opening Social Window from Login")  # Debugging Statement
        self.socialWindow = Social()  # Menginisialisasi kelas Social
        self.socialWindow.show()
        print("Social Window should be visible now")  # Debugging Statement
        self.close()

    
class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Register()  # Membuat instance dari kelas Ui_Register
        self.ui.setupUi(self)  # Menginisialisasi UI
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.adjustSize()

        # Menghubungkan tombol X (pushButton_7) ke metode close()
        self.ui.pushButton_7.clicked.connect(self.close)
        
        # Menghubungkan tombol ke metode openSocial
        self.ui.pushButton_3.clicked.connect(self.openSocial)
        self.ui.pushButton_4.clicked.connect(self.openSocial)
        self.ui.pushButton_5.clicked.connect(self.openSocial)
        self.ui.pushButton_6.clicked.connect(self.openSocial)

    def openSocial(self):
        print("Opening Social Window from Register")  # Debugging Statement
        self.socialWindow = Social()  # Menginisialisasi kelas Social
        self.socialWindow.show()
        print("Social Window should be visible now")  # Debugging Statement
        self.close()

class Social(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Social()  # Membuat instance dari kelas Ui_Register
        self.ui.setupUi(self)  # Menginisialisasi UI
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        print("Social Window Initialized")  # Debugging Statement
        self.ui.pushButton.clicked.connect(self.returnToLogin)        

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.returnToLogin)
        self.timer.start(5000)  # 3000 ms = 3 detik

    def returnToLogin(self):
        print("Returning to Login Window")  # Debugging Statement
        self.timer.stop()  # Hentikan timer
        self.loginWindow = Login()  # Menginisialisasi kembali Login
        self.loginWindow.show()
        self.close()  # Tutup window Social

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()  # Menampilkan window SplashScreen
    sys.exit(app.exec_())
