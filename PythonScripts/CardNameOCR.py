from PIL import Image

import easyocr
import numpy
import os

reader = easyocr.Reader(['en'], gpu=True)

from PIL import ImageFilter

startResolution = (822,1122)

cardSize = (745,1040)

padding = ((startResolution[0] - cardSize[0]) // 2, (startResolution[1] - cardSize[1]) // 2)

WHITELIST_CHARS = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')

def CardnameToImage(name:str) -> str:
    return ''.join(filter(WHITELIST_CHARS.__contains__, name)) + ".png"


sourceFolder = "C:/Users/cirio/Documents/Python/TrolleyCubePrintImages/Results/CustomSelf"

for file in os.listdir(sourceFolder)[57:]:

    filename = sourceFolder + "/" + file

    result = reader.readtext(filename, detail=0)

    img = Image.open(filename)

    img = img.resize((822,1122))

    img = img.crop((padding[0], padding[1], padding[0] + cardSize[0], padding[1] + cardSize[1]))

    img.save(f"../ImageFiles/TrolleyNew/{CardnameToImage(result[0])}")