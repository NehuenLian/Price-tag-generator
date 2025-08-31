from PIL import Image, ImageDraw, ImageFont

width, height = 1100, 420
color_fondo = (255, 255, 255)
canvas = Image.new("RGB", (width, height), color=color_fondo)
draw = ImageDraw.Draw(canvas)


draw.rectangle((0, 0, 1100, 190), fill="#E8E8E8")

font = ImageFont.truetype("arialbd.ttf", size=24)

# product name
draw.text((30, 50), "COCA COLA ORIGINAL 2.25LT", fill="black", font=font)

# title
draw.text((500, 10), "Precio final al consumidor", fill="black", font=font)

# product price
price_font = ImageFont.truetype("arialbd.ttf", size=70)
draw.text((500, 40), "$ 1890 ⁰⁰", fill="black", font=price_font)

# price without taxes
draw.text((500, 130), "Precio sin impuestos nacionales (IVA) $1.493.10", fill="black", font=font)

# price per liter
draw.text((500, 205), "Precio al consumidor por cada litro $945", fill="black", font=font)

# barcode image
barcode_img = Image.open("barcode.png")
x, y = 495, 230

canvas.paste(barcode_img, (x, y))

canvas.show()