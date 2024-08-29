import cv2
import os
import pandas as pd
import pykakasi
from PIL import Image, ImageDraw, ImageFont
import datetime
from paddleocr import PaddleOCR, draw_ocr, PPStructure, draw_structure_result, save_structure_res
from sudachipy import tokenizer,dictionary
from deep_translator import GoogleTranslator

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

ocr = PaddleOCR(use_angle_cls=True, 
                lang='japan', 
                use_space_char = True, 
                cls = True)

def process_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    #image preprocessing

    resized = cv2.resize(img, (0,0), fx=4, fy=4)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    thresh,im_bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    result = ocr.ocr(im_bw, cls=True)

    boxes = [line[0] for line in result[0]]
    txts = [line[1][0] for line in result[0]]
    scores = [line[1][1] for line in result[0]]
    boxes_actual = [[(int(x/4), int(y/4)) for (x, y) in box] for box in boxes] # real size coordinate

    #translate a line
    translator = GoogleTranslator(source='auto', target='en')
    translated = [translator.translate(txt) for txt in txts]

    #tokenize each word

    tokenizer_obj = dictionary.Dictionary(dict_type='full').create()
    mode = tokenizer.Tokenizer.SplitMode.B
    kks = pykakasi.kakasi()

    #version 1
    tokens = [[m.surface() for m in tokenizer_obj.tokenize(txt, mode)] for txt in txts]
    translated_token = [[translator.translate(word) for word in token] for token in tokens]
    romaji = [[''.join([item['hepburn'] for item in kks.convert(word)]) for word in token] for token in tokens]

    result = list(zip(boxes_actual, txts, translated, tokens, romaji, translated_token))

    df = pd.DataFrame(result, columns=['Box','Japanese','Translated','Tokens','Romaji','Translated_Tokens'])
    
    return resized,df

def draw_translated_text(image_path, df): # Fitur add text translate ke gambar, masih dalam pengembangan tapi fungsional
    # load gambar
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    # define font, bebas font apa, ini pake default dr pillow library
    font = ImageFont.truetype("arial.ttf", 25)
    
    # ambil box buat koordinat sama text translatenya
    for index, row in df.iterrows():
        box = row['Box']
        translated_text = row['Translated']
        print(f"Row {index}: box={box}")
        
         # ada beberapa bagian text yang bakal none, jadi diskip aja karena bikin error
        if translated_text is None:
            print(f"Skipping row {index} because translated_text is None")
            continue
        
        # gambar text dan textbox
        left, top, right, bottom = draw.textbbox(box[0], translated_text, font=font)
        draw.rectangle((left-5, top-5, right+5, bottom+5), fill="white") 
        draw.text(box[0], translated_text, fill="white", font=font, stroke_width=2, stroke_fill="black")
    
    # buat generate filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_filename = f"translated_image_{timestamp}.jpg"
    
    # buat output directory untuk save file
    output_dir = "out_image"
    os.makedirs(output_dir, exist_ok=True)
    
    # full path buat output directory
    full_path = os.path.join(output_dir, unique_filename)
    
    # save file
    image.save(full_path)
    image.show()


#example function used
#IMAGE_PATH = "./data/b.jpg"
IMAGE_PATH = "./data/y.jpg"
image, df = process_image(IMAGE_PATH)

print(df)
draw_translated_text(IMAGE_PATH, df)