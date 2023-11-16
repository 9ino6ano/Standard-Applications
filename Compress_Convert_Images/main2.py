#Select a sample image to use
from PIL import Image

img=Image.open("download.png")
image=img.convert("")

image.save("pdf_file.pdf")