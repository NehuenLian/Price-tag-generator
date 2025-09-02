from PIL import Image, ImageDraw, ImageFont

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
def create_pricetag() -> None:

    draw.rectangle((0, 0, 1100, 190), fill="#E8E8E8")

    # product name
    product_name = format_product_name("")
    draw.text((30, 50), product_name, fill="black", font=FONT)

    # title
    draw.text((500, 10), FINAl_PRICE_TITLE, fill="black", font=FONT)

    # product price
    draw.text((500, 40), "$ 1890 ⁰⁰", fill="black", font=PRICE_FONT)

    # price without taxes
    draw.text((500, 130), "Precio sin impuestos nacionales (IVA) $1.493.10", fill="black", font=FONT)

    # price per liter
    draw.text((500, 205), "Precio al consumidor por cada litro $945", fill="black", font=FONT)

    # barcode image
    barcode_img = Image.open("barcode.png")
    canvas.paste(barcode_img, (X, Y))
    
    canvas.show()