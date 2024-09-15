# src/python_scripts/resize_image.py
def resize_image(image, new_width=100, adjust_height_percentage=1):
    width, height = image.size
    ratio = (height * adjust_height_percentage) / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image
