import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout, QLabel, QLineEdit, QStackedWidget
from PyQt5.QtCore import Qt
from OCR_Final.ocr import process_image

class MainWindow(QMainWindow):
    def __init__(self, df):
        super().__init__()

        self.setWindowTitle("Dynamic Rows in Scroll Area with Stacked Widget")
        self.setGeometry(100, 100, 400, 300)

        # Create a QStackedWidget to hold different pages
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Create a first page (scroll area for rows)
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        # Create a container widget for the scroll area
        self.container = QWidget()
        self.scroll_area.setWidget(self.container)

        # Create a QVBoxLayout for the container
        self.layout = QVBoxLayout(self.container)

        # Add rows dynamically based on the DataFrame
        self.add_rows_from_dataframe(df)

        # Add the scroll area as the first page to the stacked widget
        self.stacked_widget.addWidget(self.scroll_area)

        # Add a dummy second page for demonstration purposes
        self.second_page = QLabel("This is the second page", self)
        self.second_page.setAlignment(Qt.AlignCenter)
        self.stacked_widget.addWidget(self.second_page)

        # You can switch between the pages like this:
        # self.stacked_widget.setCurrentIndex(0)  # Go to first page (scroll area)
        # self.stacked_widget.setCurrentIndex(1)  # Go to second page

    def add_rows_from_dataframe(self, df):
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
            row_widget.setStyleSheet("background-color: yellow; border: 1px solid black; margin: 5px; padding: 5px;")

            # Add the row to the main layout
            self.layout.addWidget(row_widget)

# if __name__ == "__main__":
#     # Sample DataFrame - this assumes the process_image function provides a dict-like structure
#     data = process_image("./data/w.jpg")
#     df = pd.DataFrame(data)

#     app = QApplication(sys.argv)
#     main_window = MainWindow(df)
#     main_window.show()
#     sys.exit(app.exec_())


