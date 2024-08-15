import cv2
import numpy as np
import pandas as pd
import matplotlib
import pykakasi
from PIL import Image
from paddleocr import PaddleOCR, draw_ocr, PPStructure, draw_structure_result, save_structure_res
from googletrans import Translator
from sudachipy import tokenizer,dictionary
from deep_translator import GoogleTranslator

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


ocr = PaddleOCR(use_angle_cls=True, 
                lang='japan', 
                use_space_char = True, 
                cls = True
) # need to run only once to download and load model into memory

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

    result = list(zip(boxes, txts, translated, tokens, romaji, translated_token))
    df = pd.DataFrame(result, columns=['Box','Japanese','Translated','Tokens','Romaji','Translated_Tokens'])
    
    return resized,df


#example function used
#IMAGE_PATH = "./data/b.jpg"
IMAGE_PATH = "./data/w.jpg"

image, df = process_image(IMAGE_PATH)

print(df)