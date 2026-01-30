from PIL import Image

def image_to_ascii(image, width, chars):
    original_width, original_height = image.size
    aspect_ratio = original_height / original_width
    height = int(width * aspect_ratio * 0.55)

    image = image.resize((width, height))
    image = image.convert("L")

    pixels = image.getdata()
    ascii_image = ""

    for i, pixel in enumerate(pixels):
        index = pixel * (len(chars) - 1) // 255
        ascii_image += chars[index]
        if (i + 1) % width == 0:
            ascii_image += "\n"

    return ascii_image
