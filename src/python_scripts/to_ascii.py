#  src/python_scripts/to_ascii.py
def to_ascii(pixels, width, height, ascii_chars=" .:-=+*#%@"):
    """ This returns a string of ascii characters that represent the image (https://paulbourke.net/dataformats/asciiart/) """
    line = ""
    for y in range(height):
        for x in range(width):
            gray = pixels[x, y][0]
            line += ascii_chars[gray * len(ascii_chars) // 256]
        line += "\n"
    return line
