import barcode
from barcode.writer import ImageWriter

def generate_barcode(barcode_number: str, barcode_type: str) -> None:

    """
    Generates a .png file with the barcode image using the barcode number.
    args:
    barcode_number: the barcode number, example: 590123412345
    barcode_type: the barcode type, example: ean13
    """

    options = { ## Image options, it can be adjusted as the user want
        "module_width" : 0.3,
        "module_height" : 10,
        "font_size" : 8,
        "text_distance" : 4,
        "quiet_zone" : 1,
    }

    ean = barcode.get(barcode_type, barcode_number, writer=ImageWriter())

    filename = ean.save('barcode', options)