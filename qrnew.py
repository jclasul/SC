import pandas as pd
import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFont
import qrcode

STOCK = pd.read_excel("C:/Winkel Lydia/STOCKLIJSTEN/voorbeeld VERSIE BACKUP.xlsx", sheetname="In")

IMG1 = 'scsc.jpg'
IMG2 = 'maat.jpg'
IMG12 = [np.asarray(PIL.Image.open(i).convert("L").resize((290,290))) for i in [IMG1,IMG2]]

# Set Fonts
fnt_small = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',size=15)
fnt_medium = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',size=30)
fnt_large = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',size=50)

for itemstock in STOCK.itertuples():    
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
    draw.text((470,100), MAAT, fill=0, font=fnt_medium)
    draw.text((370,100), "Maat :", fill=0, font=fnt_medium)
    draw.text((690,270), ONZE_REF, fill=0, font=fnt_small)

    for j in range(0,itemstock.Aantal):
        # Combine text and image
        IMG_NAME = 'C:/Users/Raf/Desktop/QR/' + ONZE_REF + "_" + str(j) + ".PNG"
        imgs_comb.save(IMG_NAME)





