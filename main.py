import sys
import os
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QGraphicsView, QGraphicsScene
from mainbackend import login_and_load_profile
from file_handling import select_image_file, create_bar_graph, fetch_graphing_data, copy_file, capture_picture
from ocr import process_image, draw_translated_text, delete_saved_image

# --> Splash Screen
from Splash_Screen import Ui_SplashScreen
from Login_info import Ui_Intro
from Menu import Ui_Menu
import server

os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'
os.environ['QT_SCREEN_SCALE_FACTORS'] = '1'
os.environ['QT_SCALE_FACTOR'] = '1'

# --> Global
counter = 0

# Definisi fungsi global
def GoToHome(intro):
    intro.ui.stackedWidget.setCurrentIndex(0)

def GoToRegister(intro):
    intro.ui.stackedWidget.setCurrentIndex(1)

def GoToInfo(intro):
    intro.ui.stackedWidget.setCurrentIndex(2)

def GoToSocial(intro):
    intro.ui.stackedWidget.setCurrentIndex(3)

class PageNavigator:
    def GoToHome(main_window):
        main_window.ui.stackedWidget.setCurrentIndex(0)

    def GoToProfile(main_window):
        main_window.ui.stackedWidget.setCurrentIndex(3)

    def GoToSettings(main_window):
        main_window.ui.stackedWidget.setCurrentIndex(2)

class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Drop Shadow Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setOffset(0, 0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)

        # QTimer ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(25)

        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()
            self.main = Intro()  # Memastikan Intro ada
            self.main.show()
            self.close()

        counter += 4

class Intro(QMainWindow):
    def __init__(self):
        super(Intro, self).__init__()
        self.ui = Ui_Intro()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        # Fungsi untuk ke berbagai macam halaman
        self.ui.GoToHome.clicked.connect(lambda: GoToHome(self))
        self.ui.GoToInfo.clicked.connect(lambda: GoToInfo(self))
        self.ui.gotoRegister.clicked.connect(lambda: GoToRegister(self))

        self.ui.Google.clicked.connect(lambda: GoToSocial(self))
        self.ui.Google_1.clicked.connect(lambda: GoToSocial(self))
        self.ui.Discord.clicked.connect(lambda: GoToSocial(self))
        self.ui.DC_1.clicked.connect(lambda: GoToSocial(self))
        self.ui.WA.clicked.connect(lambda: GoToSocial(self))
        self.ui.WA_1.clicked.connect(lambda: GoToSocial(self))
        self.ui.Youtube.clicked.connect(lambda: GoToSocial(self))
        self.ui.YT_1.clicked.connect(lambda: GoToSocial(self))

        # Fungsi untuk Login Button
        self.ui.Login_button.clicked.connect(self.login)

        # Fungsi untuk register Button
        self.ui.RegisterButton.clicked.connect(self.register)

        # Mengatur atribut untuk jendela utama
        self.adjustSize()

    def login(self):
        username = self.ui.inputUsername.text()
        password = self.ui.inputPassword.text()

        # Memastikan login dengan menggunakan mainbackend
        if  login_and_load_profile(username, password):
            self.menu_window = Menu()  
            self.menu_window.show()

            # Membuat dan menginisialisasi QGraphicsScene
            scene = QGraphicsScene()

            # Misalnya, kita tambahkan item ke dalam scene (contoh: persegi panjang)
            scene.addRect(10, 10, 100, 100)

            # Menetapkan scene ke graphicsView dari UI Menu
            self.menu_window.ui.graphicsView.setScene(scene) 

            # Menutup jendela login
            self.close()
        else:
            self.ui.Error.setText("Invalid username or password.")  
            self.error_timer = QtCore.QTimer(self)
            self.error_timer.setSingleShot(True)
            self.error_timer.timeout.connect(self.clear_error_message)
            self.error_timer.start(3000)

    def register(self):
        username = self.ui.inputUsername_2.text()
        password = self.ui.InputPassword.text()
        reinput = self.ui.ReInputPassword.text()

        if password == reinput:
            if server.register(username, password):
                self.ui.stackedWidget.setCurrentIndex(0)
            else:
                self.ui.Error_2.setText("Username Already Exists")
        else:
            self.ui.Error_2.setText("Passwords do not match.")
            self.error_timer = QtCore.QTimer(self)
            self.error_timer.setSingleShot(True)
            self.error_timer.timeout.connect(self.clear_error_message_register)
            self.error_timer.start(3000)

    def clear_error_message(self):
        self.ui.Error.clear()

    def clear_error_message_register(self):
        self.ui.Error_2.clear()

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        # Fungsi untuk ke berbagai macam halaman
        self.ui.Home_Button_1.clicked.connect(lambda: PageNavigator.GoToHome(self))
        self.ui.Home_button_2.clicked.connect(lambda: PageNavigator.GoToHome(self))

        self.ui.profile_Button_1.clicked.connect(lambda: PageNavigator.GoToProfile(self))
        self.ui.Profile_button_1.clicked.connect(lambda: PageNavigator.GoToProfile(self))

        self.ui.Setting_Button_1.clicked.connect(lambda: PageNavigator.GoToSettings(self))
        self.ui.Settings_button_2.clicked.connect(lambda: PageNavigator.GoToSettings(self))

        self.ui.Signout_Button_1.clicked.connect(self.close)
        self.ui.Signout_Button_2.clicked.connect(self.close)

        # Hapus atau ubah jika frame_3 tidak ada di UI Designer
        try:
            self.ui.frame_3.setHidden(True)
        except AttributeError:
            print("frame_3 tidak ada di file UI")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    window.show()  # Ensure the splash screen is shown
    sys.exit(app.exec_())
