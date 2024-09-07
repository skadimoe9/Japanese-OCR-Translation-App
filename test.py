import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout, QLabel, QLineEdit
from ocr import process_image

class MainWindow(QMainWindow):
    def __init__(self, df):
        super().__init__()

        self.setWindowTitle("Dynamic Rows in Scroll Area")
        self.setGeometry(100, 100, 400, 300)

        # Create a QScrollArea
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setGeometry(10, 10, 380, 280)
        self.scroll_area.setWidgetResizable(True)

        # Create a container widget
        self.container = QWidget()
        self.scroll_area.setWidget(self.container)

        # Create a QVBoxLayout for the container
        self.layout = QVBoxLayout(self.container)

        # Add rows dynamically based on the DataFrame
        self.add_rows_from_dataframe(df)

    def add_rows_from_dataframe(self, df):
        for index, row in df.iterrows():
            if row['Translated'] == None:
                continue    

            # Create a new row with a QLabel and QLineEdit
            row_widget = QWidget()
            row_layout = QVBoxLayout(row_widget)
            
            # Add Japanese Text
            label_japanese = QLabel(f"Japanese Text: {row['Japanese']}", row_widget)
            label_japanese.setWordWrap(True)  # Enable word wrap
            row_layout.addWidget(label_japanese)
            
            # Add Romaji
            label_romaji = QLabel("Romaji: " + " ".join(row['Romaji']), row_widget)
            label_romaji.setWordWrap(True)  # Enable word wrap
            row_layout.addWidget(label_romaji)
            
            # Add Translated Text
            label_translated = QLabel(f"Translated Text: {row['Translated']}", row_widget)
            label_translated.setWordWrap(True)  # Enable word wrap
            row_layout.addWidget(label_translated)

            # Add the row to the main layout
            self.layout.addWidget(row_widget)

if __name__ == "__main__":
    # Sample DataFrame

    data = process_image("./data/w.jpg")
    df = pd.DataFrame(data)

    app = QApplication(sys.argv)
    main_window = MainWindow(df)
    main_window.show()
    sys.exit(app.exec_())