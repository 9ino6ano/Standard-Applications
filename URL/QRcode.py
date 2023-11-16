#PYQRCOde, pypng, pyzbar, Pillow
#import pyqrcode

#text="Hello there"

#qr=pyqrcode.create(text)
#qr.png("abc.png",scale=6)


from pyzbar.pyzbar import decode
from PIL import Image

d=decode(Image.open("abc.png"))
print(d[0].data.decode("ascii"))
