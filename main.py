import sys
import os
import pandas as pd

from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGraphicsDropShadowEffect, QLabel, QPushButton, QVBoxLayout, QMessageBox, QWidget
from OCR_Final.mainbackend import login_and_load_profile, pick_image_and_run_ocr, capture_camera_ocr, save_image_decision
from OCR_Final.file_handling import delete_file
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
delete_file()

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
    image_path = None

class DialogBox(QDialog):
    def __init__(self, parent=None):
        super(DialogBox, self).__init__(parent)
        self.ui = Ui_Form()  # Use the UI from Dialog
        self.ui.setupUi(self)

    def show_confirmation_dialog(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(f"Press 'c' to capture image and 'q' to quit.")
        msg_box.setWindowTitle("Alert")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def SaveConfirmation(self):
        self.ui.stackedWidget.setCurrentIndex(1)



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
        self.setWindowTitle("日本語 OCR Translator")
        self.setWindowIcon(QIcon('./file_resources/logo_app_japaneseocr.png'))

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
        self.setWindowTitle("日本語 OCR Translator")
        self.setWindowIcon(QIcon('./file_resources/logo_app_japaneseocr.png'))

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

        self.ui.pushButton_4.clicked.connect(lambda:PageNavigator.GoToResult(self))
        self.ui.pushButton_5.clicked.connect(lambda:PageNavigator.GoToResult(self))

        self.ui.Signout_Button_1.clicked.connect(self.close)
        self.ui.Signout_Button_2.clicked.connect(self.close)

        self.ui.pushButton_7.clicked.connect(lambda:(self.pick_image_and_extract_dataframe()))

        self.ui.pushButton_14.clicked.connect(lambda:(DialogBox.show_confirmation_dialog(self),self.capture_image_and_extract_dataframe()))
        
        # Connect button_14 to open the confirmation dialog
        self.ui.frame_3.setHidden(True)

    def show_yes_no_dialog(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setText("Do you want to save image with translated text?")
        msg_box.setWindowTitle("Confirmation")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        response = msg_box.exec_()

        if response == QMessageBox.Yes:
            save_image_decision(1, ShareData.image_path)
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(f"Image saved")
            msg_box.setWindowTitle("Alert")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
        else:
            save_image_decision(0, ShareData.image_path)
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(f"Image not saved")
            msg_box.setWindowTitle("Alert")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_() 

    def add_rows_from_dataframe(self, df):
        if df is None:
            return

        for index, row in df.iterrows():
            if row['Translated'] is None:
                continue    

            # Create a new row with a QLabel and QLineEdit inside a QWidget
            row_widget = QWidget()
            row_layout = QVBoxLayout(row_widget)

            # Add Japanese Text
            label_japanese = QLabel(f"Japanese Text: {row['Japanese']}", row_widget)
            label_japanese.setWordWrap(True)
            row_layout.addWidget(label_japanese)
            
            # Add Romaji
            label_romaji = QLabel("Romaji: " + " ".join(row['Romaji']), row_widget)
            label_romaji.setWordWrap(True)
            row_layout.addWidget(label_romaji)
            
            # Add Translated Text
            label_translated = QLabel(f"Translated Text: {row['Translated']}", row_widget)
            label_translated.setWordWrap(True)
            row_layout.addWidget(label_translated)

            # Set the yellow background for the row widget
            row_widget.setStyleSheet("background-color: rgb(219, 211, 189); border: 1px solid black; margin: 5px; padding: 5px;")

            # Add the row to the main layout
            self.ui.scrollArea_2.widget().layout().addWidget(row_widget)

    def pick_image_and_extract_dataframe(self):
        ShareData.image_path, df = pick_image_and_run_ocr(ShareData.username)
        if df is None:
            return

        self.display_image("./data/temp_image.jpg", self.ui.label_12)
        self.display_image("./out_image/showFinalImage.jpg", self.ui.Hasil_gambar)
        self.add_rows_from_dataframe(df)
        PageNavigator.GoToResult(self)
        self.show_yes_no_dialog()

    def capture_image_and_extract_dataframe(self):
        ShareData.image_path, df = capture_camera_ocr(ShareData.username)
        if df is None:
            return
        self.display_image("./data/temp_image.jpg", self.ui.label_12)
        self.display_image("./out_image/showFinalImage.jpg", self.ui.Hasil_gambar)
        self.add_rows_from_dataframe(df)
        PageNavigator.GoToResult(self)
        self.show_yes_no_dialog()

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
        self.display_image("./data/temp_image.jpg", self.ui.label_12)
        self.ui.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.display_image("./graph/datalog.png", self.ui.label_8)
        self.display_image("./out_image/showFinalImage.jpg", self.ui.Hasil_gambar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    window.show()  # Ensure the splash screen is shown
    sys.exit(app.exec_())
