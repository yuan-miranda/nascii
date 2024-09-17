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
# mid: 40
# optimal: 32

WIDTH = 52

def nascii_removedirs(path):
    """ compared to os.removedirs, this function removes all files in the directory before removing the directory """
    for i in os.listdir(path):
        os.remove(f"{path}/{i}")
    os.removedirs(path)

def generate_ascii():
    """ main function to generate ascii art from video frames """
    file_name = sys.argv[1]
    video_path = f"./media/{file_name}"
    file_name = video_path.split("/")[-1].split(".")[0]
    output_path = f"./output/{file_name}"
    video_frame_path = f"{output_path}/{file_name}_frames"
    frame_resize_path = f"{output_path}/{file_name}_resize"
    frame_quantize_path = f"{output_path}/{file_name}_quantize"

    os.mkdir(output_path)
    os.mkdir(video_frame_path)
    os.mkdir(frame_resize_path)
    os.mkdir(frame_quantize_path)

    time_start = time.time()

    # extract frames from video
    to_frames(video_path, video_frame_path)
    end_frame_time = time.time() - time_start
    print(f"Extracted frames from video in {end_frame_time:.2f} seconds")

    # resize images
    for i in os.listdir(video_frame_path):
        img = Image.open(f"{video_frame_path}/{i}")
        img = resize_image(img, new_width=WIDTH, adjust_height_percentage=0.38)
        img.save(f"{frame_resize_path}/{i}")
    end_resize_time = time.time() - time_start
    print(f"Resized frames in {end_resize_time - end_frame_time:.2f} seconds")

    # quantize images to 8 bit color depth grayscale
    for i in os.listdir(frame_resize_path):
        img = Image.open(f"{frame_resize_path}/{i}")
        width, height = img.size
        pixels = img.load()
        quantize_image(pixels, width, height, n=8, grayscale=True)
        img.save(f"{frame_quantize_path}/{i}")
    end_quantize_time = time.time() - time_start
    print(f"Quantized frames in {end_quantize_time - end_resize_time:.2f} seconds")

    # convert images to ascii (already grayscale)
    for i in os.listdir(frame_quantize_path):
        img = Image.open(f"{frame_quantize_path}/{i}")
        width, height = img.size
        ascii_img = to_ascii(img.load(), width, height)
        with open(f"./output/{file_name}/{file_name}_ascii.txt", "a") as f:
            f.write(ascii_img)
            f.write("END\n")
    end_ascii_time = time.time() - time_start
    print(f"Converted frames to ascii in {end_ascii_time - end_quantize_time:.2f} seconds")

    # delete the directories
    nascii_removedirs(video_frame_path)
    nascii_removedirs(frame_resize_path)
    nascii_removedirs(frame_quantize_path)

    print(f"Toral time: {time.time() - time_start:.2f} seconds")
    print("Done!")

def main():
    generate_ascii()
    
if __name__ == "__main__":
    main()
