from tool.barcode_generator import generate_barcode
from tool.generate_pricetag import create_pricetag

def main():
    generate_barcode('7790895000997', 'ean13') ## example data
    create_pricetag("COCA COLA SABOR ORIGINAL 2.25L", 
                    3852.81,
                    2892.56,
                    945)

if __name__ == "__main__":
    main()