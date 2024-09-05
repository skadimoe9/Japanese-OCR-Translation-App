# cari cara untuk dapet waktu hari ini
# bikin dataframe (kolom pertama itu bulan tanggal), kolom kedua jumlah karakter dalam satu kalimat 

import numpy as np
from ocr import process_image, draw_translated_text
from datetime import datetime

import numpy as np
import pandas as pd
from datetime import datetime

class TranslationDataStore:
    def __init__(self):
        self.translation_counts = []
        self.timestamps = []

    def separate_and_count_characters(self, df):
        """
        Separate each character from the Japanese text in txts and count the number of characters
        that have been successfully translated.
        
        Args:
        df (pd.DataFrame): DataFrame containing the txts and translated columns.
        
        Returns:
        int: Number of Japanese characters successfully translated.
        str: Timestamp (day/month/year) when the translation was done.
        """
        # Extract txts and translated columns
        txts = df['Japanese'].tolist()
        translated = df['Translated'].tolist()
        
        # Separate each character from the Japanese text
        separated_characters = [char for sentence in txts for char in sentence]
        
        # Count the number of characters that have been successfully translated
        translated_characters_count = sum(1 for t in translated if t is not None)
        chara_count = len(separated_characters)
        
        # Get the current timestamp (day/month/year)
        timestamp = datetime.now().strftime("%d/%m/%Y")
        
        return chara_count, timestamp

    def store_translation_data(self, df):
        """
        Store the number of Japanese characters successfully translated and the timestamp in arrays.
        
        Args:
        df (pd.DataFrame): DataFrame containing the txts and translated columns.
        
        Returns:
        np.ndarray: Array of the number of Japanese characters successfully translated.
        list: List of timestamps when the translations were done.
        """
        # Get the translation data
        count, timestamp = self.separate_and_count_characters(df)
        
        # Store the data in arrays
        self.translation_counts.append(count)
        self.timestamps.append(timestamp)
        
        # Convert translation_counts to a NumPy array
        translation_counts_array = np.array(self.translation_counts)
        
        return translation_counts_array, self.timestamps

data_store = TranslationDataStore()
PATHIMG2 = "./data/w.jpg"
df2 = process_image(PATHIMG2)
print(df2)
draw_translated_text(PATHIMG2, df2)
characters, tstamps = data_store.store_translation_data(df2)
print("Translation Counts:", characters)
print("Timestamps:", tstamps)