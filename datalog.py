# cari cara untuk dapet waktu hari ini
# bikin dataframe (kolom pertama itu bulan tanggal), kolom kedua jumlah karakter dalam satu kalimat 

from ocr import process_image, draw_translated_text, delete_saved_image
from file_handling import create_bar_graph, fetch_graphing_data
from datetime import datetime
from server import update_daily_data 

def separate_and_count_characters(df):
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