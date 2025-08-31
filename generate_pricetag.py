from PIL import Image, ImageDraw, ImageFont

img = Image.open('barcode.png')

img.save('barcode.jpg')
img.convert('L').save('barcode_bw.png')