from os import name
from re import template
import pandas as pd
import code128
from numpy import column_stack, nan
from PIL import Image, ImageFont, ImageDraw 
from PyPDF2 import PdfFileMerger, PdfFileReader
from time import sleep


data = pd.read_excel (r'C:/Users/inci1/Desktop/liste.xlsx',dtype=str,convert_float=1,index_col=None,header=None)

imei = data[0].tolist()
imei = [item for item in imei if not(pd.isnull(item)) == True]

for i in range(len(imei)):

    barkod = code128.image(imei[i])
    bw, bh = barkod.size
    #barkod=barkod.crop((27, 0, bw-27, bh))
    barkod=barkod.resize([int(bw/1.2),bh])
    template1= Image.open('C:/Users/inci1/Desktop/blank.png')

    tw,th = template1.size

    imei_font = ImageFont.truetype('C:/Users/inci1/Documents/barkcodemaker/regular.ttf', 35)

    template1.paste(barkod,(0  , 60))
    template1.paste(barkod,(0, 90))

    image_editable = ImageDraw.Draw(template1)
    
    image_editable.text((95,200), (imei[i]), (0), font=imei_font,stroke_width=1,)
    image_editable.text((150,5), ("T15 Black"), (0), font=imei_font,stroke_width=1,)


    template1.save("C:/Users/inci1/Documents/barkcodemaker/pdfs/bcs_"+str(i)+".pdf")

mergedObject = PdfFileMerger()

for i in range(len(imei)):
    mergedObject.append(PdfFileReader('C:/Users/inci1/Documents/barkcodemaker/pdfs/bcs_' + str(i)+ '.pdf', 'rb'))
 
mergedObject.write("C:/Users/inci1/Desktop/liste.pdf")
