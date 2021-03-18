import cv2
import numpy as np
import pandas as pd
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"

img = cv2.imread('RPA/2017/028-7226263-1633148.JPG')

# gets top and left coordinates of every recognized word
d = pytesseract.image_to_data(img, output_type=Output.DICT)
list = [[d['text'][i], d['top'][i], d['left'][i]] for i in range(len(d['text'])) if d['text'][i] != '']
table = pd.DataFrame(np.array(list), columns=['WORD', 'TOP', 'LEFT'])
print(table.head(10))

# draws bounding boxes around each recognized word
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('img', img)
cv2.waitKey(0)

