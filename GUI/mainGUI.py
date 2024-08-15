import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect,QWidget

# --> Splash Screen
from Splash_Screen import Ui_SplashScreen

from Main_menu import Ui_Form

# --> Global
counter = 0


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()  # Membuat instance dari kelas Ui_SplashScreen
        self.ui.setupUi(self)  # Menginisialisasi UI

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

        #QTimer ==>START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        
        self.show()  # Menampilkan jendela splash screen

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)

        if counter >100:
            self.timer.stop()
            self.main = Form()
            self.main.show()

            self.close()

        counter +=1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()  # Menampilkan window SplashScreen
    sys.exit(app.exec_())
