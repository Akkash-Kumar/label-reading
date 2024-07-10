try:

    from PIL import Image

except ImportError:

    import Image

import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'    #filepath where tesseract ocr is installed

def recText(filename):

    text = pytesseract.image_to_string(Image.open(filename))    #open file and read string

    return text

info = recText('test2.jpg')


file = open("Result1.txt",'w')    #create new text file in write mode 


file.write(info)   #store text from image

file.close()  #close file

print("Created successfully")  
