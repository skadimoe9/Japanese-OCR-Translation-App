import sys
import os
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGraphicsDropShadowEffect, QLabel, QPushButton, QVBoxLayout
from OCR_Final.mainbackend import login_and_load_profile, pick_image_and_run_ocr, capture_camera_ocr
import OCR_Final.file_handling
from OCR_Final.ocr import delete_saved_image


# --> Splash Screen
from GUI_Final.Splash_Screen import Ui_SplashScreen
from GUI_Final.Login_info import Ui_Intro
from GUI_Final.Menu import Ui_Menu
from OCR_Final.server import register
from GUI_Final.Dialog import Ui_Form

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
   
    def GoToResult(main_window):
        main_window.ui.stackedWidget.setCurrentIndex(1)

class ShareData:
    username = None
    user_id = None


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
        ShareData.username = self.ui.inputUsername.text()
        password = self.ui.inputPassword.text()

        status, ShareData.user_id = login_and_load_profile(ShareData.username, password)
        # Memastikan login dengan menggunakan mainbackend
        if status:
            self.menu_window = Menu()  
            self.menu_window.show()

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
            if register(username, password):
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

        # Menampilkan username dan user_id
        self.ui.Username_Box.setText(f"{ShareData.username}")
        self.ui.userID_box.setText(f"{ShareData.user_id}")

        # Fungsi untuk ke berbagai macam halaman
        self.ui.Home_Button_1.clicked.connect(lambda: PageNavigator.GoToHome(self))
        self.ui.Home_button_2.clicked.connect(lambda: PageNavigator.GoToHome(self))

        self.ui.profile_Button_1.clicked.connect(lambda: PageNavigator.GoToProfile(self))
        self.ui.Profile_button_1.clicked.connect(lambda: PageNavigator.GoToProfile(self))
        self.ui.pushButton_2.clicked.connect(lambda: PageNavigator.GoToProfile(self))

        self.ui.Setting_Button_1.clicked.connect(lambda: PageNavigator.GoToSettings(self))
        self.ui.Settings_button_2.clicked.connect(lambda: PageNavigator.GoToSettings(self))

        self.ui.Signout_Button_1.clicked.connect(self.close)
        self.ui.Signout_Button_2.clicked.connect(self.close)
        self.ui.pushButton_7.clicked.connect(lambda:(pick_image_and_run_ocr(ShareData.username),PageNavigator.GoToResult(self)))
        self.ui.pushButton_14.clicked.connect(lambda:(capture_camera_ocr(ShareData.username),PageNavigator.GoToResult(self)))
        # Connect button_14 to open the confirmation dialog


        self.ui.frame_3.setHidden(True)

        # Menampilkan gambar di label_8 (pastikan label_8 adalah QLabel)
    def display_image(self, image_path, label):
        """Function to display and scale image."""
        if os.path.exists(image_path):
            final_image = QPixmap(image_path)
            # Scale the image to fit the label dimensions
            scaled_pixmap = final_image.scaled(
                label.width(),  # Sesuaikan dengan lebar label
                label.height(),  # Sesuaikan dengan tinggi label
                QtCore.Qt.KeepAspectRatio,
                QtCore.Qt.SmoothTransformation
            )
            label.setPixmap(scaled_pixmap)  # Atur gambar di label
        else:
             print(f"Path gambar tidak ditemukan: {image_path}")

    def resizeEvent(self, event):
        """Handle the resizing of the window to adjust image scaling."""
        super(Menu, self).resizeEvent(event)
        # Refresh the image size when the window is resized
        self.display_image("./graph/datalog.png", self.ui.label_8)
        self.display_image("./out_image/showFinalImage.jpg", self.ui.Hasil_gambar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    window.show()  # Ensure the splash screen is shown
    sys.exit(app.exec_())
