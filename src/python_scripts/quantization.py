# src/python_scripts/quantization.py
def quantize_color(color, n=8):
    return int(color / 256 * n) * int(256 / n)

def quantize_pixel(r, g, b, n=8, grayscale=False):
    if grayscale:
        r = g = b = int(0.299 * r + 0.587 * g + 0.114 * b)
    return (quantize_color(r, n), quantize_color(g, n), quantize_color(b, n))

def quantize_image(pixels, width, height, n=8, grayscale=False):
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]
            pixels[x, y] = quantize_pixel(r, g, b, n, grayscale)

def grayscale_image(pixels, width, height):
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]
            pixels[x, y] = (int(0.299 * r + 0.587 * g + 0.114 * b),) * 3
