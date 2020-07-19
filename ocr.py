import pytesseract 
import cv2 
import os 
import numpy as np 
from docx import Document 
from PIL import Image,ImageEnhance 
def tesseract(filename): 
im = Image.open(filename) 
rgb_im = im.convert('RGB') 
rgb_im.save("test.jpg", dpi=(300,300)) 
image_dpi = cv2.imread('test.jpg',0) 
os.remove("test.jpg") 
blur = cv2.bilateralFilter(image_dpi,15,75,75)
2.THRESH_BINARY,11,2) 
ret3,th3cv2.threshold 
(th3,0,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C+cv2.THRESH_OTSU) 
imagem = cv2.bitwise_not(th3) 
kernel = np.ones((1,1),np.uint8) 
eroded_img = cv2.erode(imagem,kernel,iterations = 1) 
#canny=cv2.Canny(imagem,100,200) 
config = ('-l eng --oem 1 --psm 3') 
text = pytesseract.image_to_string(eroded_img, config=config) 
return text 
test_file = tesseract(filename='C:\\Users\\dell-pc\\Desktop\\scan4.png') 
document = Document() 
document.add_paragraph(test_file) 
document.save('test.docx')
