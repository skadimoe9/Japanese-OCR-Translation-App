import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout, QLabel, QLineEdit, QStackedWidget
from PyQt5.QtCore import Qt
from OCR_Final.ocr import process_image

def add_rows_from_dataframe(self, df):
    try:
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

    except AttributeError:
        print("No data to show.")

