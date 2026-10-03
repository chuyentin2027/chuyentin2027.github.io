import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import fitz
import pytesseract
from PIL import Image
import io

os.environ['TESSDATA_PREFIX'] = r'e:\DeThiChuyenTin\tessdata'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

test_file = r'e:\DeThiChuyenTin\dethi\An_Giang_2020_-_2021_e_thi_tuyen_sinh_lop_10_chuyen_tin_tinh_An_Giang_nam_2020.pdf'
print('Testing with file:', test_file)

doc = fitz.open(test_file)
print('Total pages:', len(doc))

for i, page in enumerate(doc):
    print(f'--- Page {i+1} ---')
    raw_text = page.get_text().strip()
    if len(raw_text) > 100:
        print('Native text (first 300 chars):')
        print(raw_text[:300])
    else:
        mat = fitz.Matrix(2.0, 2.0)
        pix = page.get_pixmap(matrix=mat)
        img = Image.open(io.BytesIO(pix.tobytes('png')))
        ocr_text = pytesseract.image_to_string(img, lang='vie+eng')
        print('OCR Text (first 300 chars):')
        print(ocr_text[:300])
