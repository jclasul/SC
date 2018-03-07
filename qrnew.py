import pandas as pd
import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFont
import qrcode

stock = pd.read_csv("C:/Users/JCLA/Downloads/DATABASE_IN - Form responses 1.csv")
stock = stock[stock["LABELED"]!=True]

# Convert and Format DATABASE
stock["Timestamp"] = pd.to_datetime(stock.Timestamp)
stock["IDnr"] = stock.Timestamp.apply(lambda x: x.timestamp())

IMG1 = 'scsc.jpg'
IMG2 = 'maat.jpg'
IMG12 = [np.asarray(PIL.Image.open(i).convert("L").resize((290,290))) for i in [IMG1,IMG2]]

# Set Fonts
fnt_small = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',size=15)
fnt_medium = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',size=30)
fnt_large = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',size=50)

for itemstock in stock.itertuples():    
    MAAT = str(itemstock.Maat)
    MERK = str(itemstock.Merk)
    PRIJS = "€" + str(itemstock.VerkoopPrijs)
    ARTICLE_NR = str(itemstock.LeverancierReferentie)
    ONZE_REF = str(itemstock.OnzeReferentie)

    QR = {'Maat':MAAT,'Merk':MERK,'Prijs':PRIJS,'Article_nr':ARTICLE_NR,'Reference_nr':ONZE_REF}
    QRCODE = qrcode.make(QR).convert("L").resize((290,290))
    imgs = [IMG12[0],IMG12[1],QRCODE]        
    imgs_comb = PIL.Image.fromarray(np.hstack([i for i in imgs]))

    # Get drawing context
    draw = ImageDraw.Draw(imgs_comb)

    # Draw text
    draw.text((355,160), PRIJS, fill=0, font=fnt_large)
    draw.text((460,100), MAAT, fill=0, font=fnt_medium)
    draw.text((360,100), "Maat :", fill=0, font=fnt_medium)
    draw.text((700,270), ONZE_REF, fill=0, font=fnt_small)
           
    for maat in maten.columns:
        for n in range(maten.loc[:,maat][0]):
            print(maat, n)
            # Combine text and image
            IMG_NAME = 'QRcodes/' + MERK + "_" + ONZE_REF + "_" + str(j+1) + ".PNG"
            imgs_comb.save(IMG_NAME)
