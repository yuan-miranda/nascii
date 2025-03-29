import sys
import os
from PIL import Image
import time
from main import to_frames, resize_image, quantize_image, to_ascii

WIDTH = 32
HEIGHT_PERCENTAGE = 0.38
BIT_DEPTH = 8
FILE = None

def main():
    global FILE
    if len(sys.argv) > 1:
        FILE = sys.argv[1]
    elif FILE is None:
        files = os.listdir("media")
        if not files:
            return print("No files found in /media directory.")
        
        for i, file in enumerate(files):
            print(f"{i}: {file}")
        
        try:
            choice = int(input("> "))
            if choice < 0 or choice >= len(files):
                raise ValueError()
            time.sleep(0.5)
            FILE = files[choice]
        except ValueError:
            return print(f"Invalid or out of range. Selection must be between 0 and {len(files) - 1}.")

    if not os.path.exists(f"media/{FILE}"):
        return print(f"{FILE} does not exist.")

    file_name = os.path.splitext(FILE)[0]

    if os.path.exists(f"output/{file_name}"):
        return print(f"{file_name} already converted.")

    output_path = f"output/{file_name}"
    output_path_frames = f"{output_path}/frames"
    os.makedirs(output_path_frames, exist_ok=True)

    time_start = time.time()

    to_frames(f"media/{FILE}", output_path_frames)
    frames = sorted(os.listdir(output_path_frames), key=lambda x: int(os.path.splitext(x)[0]))

    # resize image
    for i in frames:
        img = Image.open(f"{output_path_frames}/{i}")
        img = resize_image(img, WIDTH, HEIGHT_PERCENTAGE)
        img.save(f"{output_path_frames}/{i}")

    # quantize image to 8 bit color
    for i in frames:
        img = Image.open(f"{output_path_frames}/{i}")
        width, height = img.size
        pixels = img.load()
        quantize_image(pixels, width, height, grayscale=True)
        img.save(f"{output_path_frames}/{i}")
    
    with open(f"{output_path}/{file_name}.txt", "w") as f:
        for i in frames:
            img = Image.open(f"{output_path_frames}/{i}")
            width, height = img.size
            ascii_img = to_ascii(img.load(), width, height)
            f.write(ascii_img)
            f.write("END\n")

    print(f"Converted frames to ascii in {time.time() - time_start:.2f} seconds")

if __name__ == "__main__":
    main()