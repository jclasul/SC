import pandas as pd
import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFont
import qrcode

stock = pd.read_csv("C:/Users/JCLA/Downloads/DATABASE_IN - Form responses 1 (3).csv")
# stock = stock[stock["LABELED"]!=True]

# Convert and Format DATABASE
stock["Timestamp"] = pd.to_datetime(stock.Timestamp, dayfirst=True)
stock["IDnr"] = stock.Timestamp.apply(lambda x: x.timestamp())

IMG1 = 'scsc.jpg'
IMG2 = 'maat.jpg'
IMG12 = [np.asarray(PIL.Image.open(i).convert("L").resize((290,290))) for i in [IMG1,IMG2]]

# Set Fonts
fnt_small = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',size=15)
fnt_medium = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',size=30)
fnt_large = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',size=50)

for itemstock in stock.itertuples():
    Merk = str(itemstock.Merk)   
    IDnr = str(itemstock.IDnr)
    VerkoopPrijs = str(itemstock.VerkoopPrijs) 

    # Google Forms URLs
    url_start = "https://docs.google.com/forms/d/e/1FAIpQLSfxJE74YdD7KoYasdWXEa1VFpTONJf79L3juT2goonwyhSzZA/viewform?usp=pp_url&entry.406303456&entry.184234757="
    url_mid = "&entry.1724678309="
    url_mid2 = "&entry.113696914="
    url_end = "&entry.72186599&entry.77984989&entry.516085731"

    # Get all sizes and quantities to generate pre-filled Google Form URL QRs
    maten = stock.loc[:,stock.columns.str.contains("Maat")].dropna(axis=1)   

    for maat in maten.columns:
        for n in range(maten.loc[:,maat][0]):
            # create link to google form
            maat_string = maat.split("[")[-1].strip("]")
            full_url_list = [url_start, IDnr, url_mid, VerkoopPrijs, url_mid2, maat_string, url_end]
            full_url = "".join(full_url_list)

            QRCODE = qrcode.make(full_url).convert("L").resize((290,290))
            imgs = [IMG12[0],IMG12[1],QRCODE]        
            imgs_comb = PIL.Image.fromarray(np.hstack([i for i in imgs]))

            # Get drawing context
            draw = ImageDraw.Draw(imgs_comb)

            # Draw text
            draw.text((355,160), " ".join(["€",VerkoopPrijs]), fill=0, font=fnt_large)
            draw.text((360,100), maat, fill=0, font=fnt_medium)
            draw.text((690,272), IDnr, fill=0, font=fnt_small)

            # Combine text and image
            IMG_NAME = 'QRcodes/' + Merk + "_" + IDnr + "_" + maat_string + "_" + str(n+1) + ".PNG"
            imgs_comb.save(IMG_NAME)
    
    
    
    



    





