from PIL import Image, ImageDraw, ImageFont
from decimal import Decimal

# ========================
# Canvas config
# ========================
WIDTH, HEIGHT = 1100, 420
BACKGROUND_COLOR = (255, 255, 255)

canvas = Image.new("RGB", (WIDTH, HEIGHT), color=BACKGROUND_COLOR)
draw = ImageDraw.Draw(canvas)

FONT = ImageFont.truetype("arialbd.ttf", size=24)
PRICE_FONT = ImageFont.truetype("arialbd.ttf", size=70)
FINAl_PRICE_TITLE = "Precio final al consumidor"

# Barcode config
X = 495
Y = 230

# ========================
# Product name format
# ========================
def format_product_name(product_name: str) -> str:
    product_name_splitted = product_name.split(" ")

    for i in range(len(product_name_splitted)):

        if i % 3 == 0:
            product_name_splitted[i] = f'\n{product_name_splitted[i]}'

    return " ".join(product_name_splitted)

# ========================
# Create and place elements in canvas
# ========================
def create_pricetag(product_name: str, 
                    product_price: Decimal, 
                    price_without_taxes: Decimal, 
                    price_per_liter: Decimal = None) -> None:

    draw.rectangle((0, 0, 1100, 190), fill="#E8E8E8")

    # product name
    formatted_product_name = format_product_name(product_name)
    draw.text((30, 50), formatted_product_name, fill="black", font=FONT)

    # tag title
    draw.text((500, 10), FINAl_PRICE_TITLE, fill="black", font=FONT)

    # product price
    draw.text((500, 40), f"${product_price}", fill="black", font=PRICE_FONT)

    # price without taxes
    draw.text((500, 130), f"Precio sin impuestos nacionales (IVA) ${price_without_taxes}", fill="black", font=FONT)

    # price per liter, display only if its passed as parameter  
    if price_per_liter:
        draw.text((500, 205), f"Precio al consumidor por cada litro ${price_per_liter}", fill="black", font=FONT)

    # embed barcode image in canvas
    barcode_img = Image.open("barcode.png")
    canvas.paste(barcode_img, (X, Y))
    
    canvas.show()