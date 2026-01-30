from PIL import ImageOps, ImageFilter, ImageEnhance

def apply_filters(image, filters):
    for f in filters:
        if f == "grayscale":
            image = image.convert("L")
        elif f == "invert":
            image = ImageOps.invert(image)
        elif f == "blur":
            image = image.filter(ImageFilter.BLUR)
        elif f == "contrast":
            image = ImageEnhance.Contrast(image).enhance(2.0)
    return  image