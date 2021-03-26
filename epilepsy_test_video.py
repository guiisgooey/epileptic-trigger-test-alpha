import cv2
import os
from io import BytesIO
from PIL import Image, ImageStat

def video_frame_test(file_path, threshold=5):
    """frame test, modified to work with video files"""
    e = False
    cap = cv2.VideoCapture(file_path)
    x = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    subpath = os.path.splitext(file_path)[0]
    last = None
    for n in range(x):
        _, image = cap.read()
        _, buf = cv2.imencode(".png", image)
        frame_obj = BytesIO(buf)        
        frame = Image.open(frame_obj)
        brightness = ImageStat.Stat(frame)
        current = brightness.rms[0]
        if last is not None:
            if (current > (last + last/threshold)) or (current < last - last/threshold):
                e = True
        last = brightness.rms[0]
    return e

def check_file(file_path):
    pass