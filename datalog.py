# cari cara untuk dapet waktu hari ini
# bikin dataframe (kolom pertama itu bulan tanggal), kolom kedua jumlah karakter dalam satu kalimat 

from ocr import process_image

IMAGE_PATH = "./data/w.jpg"
image, df = process_image(IMAGE_PATH)
print(df)