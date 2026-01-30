from PIL import Image
from ascii_art.filters import apply_filters

def converte_image_to_ascii(
    image_path: str,
    width: int = 100,
    chars: str = "@#*+=-:. ",
    filters: list = None
) -> str:
    image = Image.open(image_path)

    #Aplicam filtrele daca exista
    if filters:
        image = apply_filters(image, filters)

    #Calcul dimensiuni pastrand proportiile
    original_width, original_height = image.size
    aspect_ratio = original_height / original_width
    height = int(width * aspect_ratio * 0.55)
    image = image.resize((width, height))

    #Convertim la grayscale daca nu e deja
    if image.mode != "L":
        image = image.convert("L")

    pixels = image.getdata()
    ascii_image = ""

    for i, pixel in enumerate(pixels):
        index = pixel * (len(chars) - 1) // 255
        ascii_image += chars[index]
        if (i + 1) % width == 0:
            ascii_image += "\n"

    return ascii_image
