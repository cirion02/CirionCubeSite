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


sourceFolder = "C:/Users/cirio/Documents/Python/TrolleyCubePrintImages/Results/BonusSheet"

for file in os.listdir(sourceFolder):

    if not file in ["Darkpact.png", "mb2-999-JEO-jund-em-out.png", "Throne of Knowledge.png", "The Pleasant Taxer.png", "Eladamri.png", "Fragment Reality (1dHnfjwiayJlbGxF3hOFhihJr4wvTIxsV).jpg", "Hells Caretaker.png", "Saiba Syphoner (1nf6am4-IeutB-4ijfw8VUFEcpbT_5NqL).jpg", "UlgrothaCharm.png"]:
        continue

    filename = sourceFolder + "/" + file

    result = reader.readtext(filename, detail=0)

    img = Image.open(filename)

    img = img.resize((822,1122))

    img = img.crop((padding[0], padding[1], padding[0] + cardSize[0], padding[1] + cardSize[1]))

    img.save(f"../ImageFiles/TrolleyBonus/{CardnameToImage(result[0])}")