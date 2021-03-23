import cv2
import os
from PIL import Image, ImageStat

def video_frame_test(file_path, threshold=5):
    """frame test, modified to work with video files"""
    e = False
    cap = cv2.VideoCapture(file_path)
    x = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    subpath = os.path.splitext(file_path)[0]
    last = None
    for n in range(x):
        if (e == True):
            os.remove(f"{subpath}_frame_{n-1}.png")
            break
        _, image = cap.read()
        cv2.imwrite(f"{subpath}_frame_{n}.png", image)        
        frame = Image.open(f"{subpath}_frame_{n}.png")
        if os.path.exists(f"{subpath}_frame_{n-1}.png"):
            os.remove(f"{subpath}_frame_{n-1}.png")
        brightness = ImageStat.Stat(frame)
        current = brightness.rms[0]
        if last is not None:
            if (current > (last + last/threshold)) or (current < last - last/threshold):
                e = True
        if n == (x-1):
             os.remove(f"{subpath}_frame_{n}.png")
        last = brightness.rms[0]
    return e