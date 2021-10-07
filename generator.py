from os import name
from re import template
import pandas as pd
import code128
from numpy import column_stack, nan
from PIL import Image, ImageFont, ImageDraw 
from PyPDF2 import PdfFileMerger, PdfFileReader
from time import sleep

imei = [2647326962]
for j in range (4999):
    imei.append(imei[j]+1)
for m in range(len(imei)):
    imei[m]='LS05B'+str(imei[m])

for i in range(len(imei)):

    barkod = code128.image(imei[i])
    bw, bh = barkod.size
    #barkod=barkod.crop((27, 0, bw-27, bh))
    barkod=barkod.resize([int(bw/1.06),bh])
    template1= Image.open('C:/Users/inci1/Desktop/blank.png')

    tw,th = template1.size

    imei_font = ImageFont.truetype('C:/Users/inci1/Documents/barkcodemaker/regular.ttf', 35)

    template1.paste(barkod,(0  , 60))
    template1.paste(barkod,(0, 90))

    image_editable = ImageDraw.Draw(template1)
    
    image_editable.text((95,200), (imei[i]), (0), font=imei_font,stroke_width=1,)
    image_editable.text((170,5), ("LS05 Black"), (0), font=imei_font,stroke_width=1,)


    template1.save("C:/Users/inci1/Documents/barkcodemaker/pdfs/bcs_"+str(i)+".pdf")

mergedObject = PdfFileMerger()

for i in range(len(imei)):
    mergedObject.append(PdfFileReader('C:/Users/inci1/Documents/barkcodemaker/pdfs/bcs_' + str(i)+ '.pdf', 'rb'))
 
mergedObject.write("C:/Users/inci1/Desktop/liste.pdf")
