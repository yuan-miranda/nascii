# src/python_scripts/to_frames.py
import os
import cv2

def to_frames(video, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video)
    if not cap.isOpened():
        print(f"Error: Could not open video {video}")
        return
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(f"{output_folder}/{frame_count}.jpg", frame)
        frame_count += 1
    cap.release()
    print(f"Extracted {frame_count} frames from {video}")
