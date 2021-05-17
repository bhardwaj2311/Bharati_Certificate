from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('list.csv')
font = ImageFont.truetype('arial.ttf',60)
organizer=str(input("Who is the organizer? "))
for index,j in df.iterrows():
    img = Image.open('certificate_template.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(1000,1250),text='{}'.format(j['Name']),fill=(0,0,0),font=font)
    draw.text(xy=(2050,1250),text='{}'.format(j['University']),fill=(0,0,0),font=font)
    draw.text(xy=(2600,1400), text = organizer,fill=(0,0,0),font=font)
    draw.text(xy=(410,1563), text='{}'.format(j['Date']), fill=(0, 0, 0), font=font)
    img.save('pictures/{}.jpg'.format(j['Name']))