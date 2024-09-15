# src/main.py
import sys
sys.path.append("./src/python_scripts")

import os
from PIL import Image
import time
from python_scripts.quantization import quantize_image
from python_scripts.resize_image import resize_image
from python_scripts.to_ascii import to_ascii
from python_scripts.to_frames import to_frames

# discord brookiecookie679
# max: 52
# mid: 48
# optimal: 32

WIDTH = 52
VIDEO_PATH = "./media/brookiecookie679.mov"
FILE_NAME = VIDEO_PATH.split("/")[-1].split(".")[0]
VIDEO_FRAME_PATH = f"./output/{FILE_NAME}/{FILE_NAME}_frames"
FRAME_RESIZE_PATH = f"{VIDEO_FRAME_PATH}/../{FILE_NAME}_resize"
FRAME_QUANTIZE_PATH = f"{FRAME_RESIZE_PATH}_8colors_grayscale"
FRAME_ASCII_PATH = f"{FRAME_QUANTIZE_PATH}_ascii"

def main():
    os.makedirs("./output", exist_ok=True)
    os.makedirs(FRAME_RESIZE_PATH, exist_ok=True)
    os.makedirs(FRAME_QUANTIZE_PATH, exist_ok=True)
    os.makedirs(FRAME_ASCII_PATH, exist_ok=True)
    print(f"./output\n{VIDEO_FRAME_PATH}\n{FRAME_RESIZE_PATH}\n{FRAME_QUANTIZE_PATH}\n{FRAME_ASCII_PATH}")

    time_start = time.time()

    # extract frames from video
    to_frames(VIDEO_PATH, VIDEO_FRAME_PATH)
    end_frame_time = time.time() - time_start
    print(f"Extracted frames from video in {end_frame_time:.2f} seconds")

    # resize images
    for i in os.listdir(VIDEO_FRAME_PATH):
        img = Image.open(f"{VIDEO_FRAME_PATH}/{i}")
        img = resize_image(img, new_width=WIDTH, adjust_height_percentage=0.38)
        img.save(f"{FRAME_RESIZE_PATH}/{i}")
    end_resize_time = time.time() - time_start
    print(f"Resized frames in {end_resize_time - end_frame_time:.2f} seconds")

    # quantize images to 8 bit color depth grayscale
    for i in os.listdir(FRAME_RESIZE_PATH):
        img = Image.open(f"{FRAME_RESIZE_PATH}/{i}")
        width, height = img.size
        pixels = img.load()
        quantize_image(pixels, width, height, n=8, grayscale=True)
        img.save(f"{FRAME_QUANTIZE_PATH}/{i}")
    end_quantize_time = time.time() - time_start
    print(f"Quantized frames in {end_quantize_time - end_resize_time:.2f} seconds")

    # convert images to ascii (already grayscale)
    for i in os.listdir(FRAME_QUANTIZE_PATH):
        img = Image.open(f"{FRAME_QUANTIZE_PATH}/{i}")
        width, height = img.size
        ascii_img = to_ascii(img.load(), width, height)
        with open(f"{FRAME_ASCII_PATH}/{FILE_NAME}.txt", "a") as f:
            f.write(ascii_img)
            f.write("END\n")
    end_ascii_time = time.time() - time_start
    print(f"Converted frames to ascii in {end_ascii_time - end_quantize_time:.2f} seconds")

    print(f"Toral time: {time.time() - time_start:.2f} seconds")
    print("Done!")

if __name__ == "__main__":
    main()