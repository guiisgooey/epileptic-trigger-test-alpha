import os
from os.path import isfile
import urllib
import urllib.request
from io import BytesIO
from PIL import Image, ImageStat

def frame_test(file_path, threshold=5):
    """Converts gif/video into individual frames and compares frames to see if it is flashing"""
    e = False
    x = 0
    last = None
    check_gif(file_path)
    if(isurl(file_path)):
        file_path = BytesIO(urllib.request.urlopen(file_path).read())
    im = Image.open(file_path)
    x = im.n_frames
    for i in range(x):
        im.seek(i)
        frames_obj = BytesIO()
        im.save(frames_obj, 'PNG')
        frame = Image.open(frames_obj)
        brightness = ImageStat.Stat(frame)
        current = brightness.rms[0]
        if last is not None:
            if (current > (last + last/threshold)) or (current < last - last/threshold):
                e = True
        last = brightness.rms[0]
    return e

def split_test(file_path, n=1):
    """Quarters gif n times and compares quartered frames using frame test"""
    e = False
    if(isurl(file_path)):
        file_path = BytesIO(urllib.request.urlopen(file_path).read())
    im = Image.open(file_path)
    w, h = im.size
    quarters = [(0, 0, w/2, h/2),(w/2, h/2, w, h), (w/2, 0, w, h/2), (0, h/2, w/2, h)]
    i = 0
    while e == False and i in range(4):
        left, top, right, bottom = quarters[i]
        e = quarter_gif_test(file_path, left, top, right, bottom, n)
        i += 1 
    return e

def quarter_gif_test(file_path, left, top, right, bottom, n=1):
    """Quarters gifs into quarter-gifs n times"""
    e = False
    check_gif(file_path)
    if(isurl(file_path)):
        file_path = BytesIO(urllib.request.urlopen(file_path).read())
    im = Image.open(file_path)
    x = im.n_frames
    frames = list()
    for i in range(x):
        if e == True:
            return e
        im.seek(i)
        frame_obj = BytesIO()
        cropped_frame_obj = BytesIO()
        im.save(frame_obj, format='PNG')
        frame = Image.open(frame_obj)
        frame = frame.crop((left, top, right, bottom))
        frame.save(cropped_frame_obj, format='PNG')
        frame = Image.open(cropped_frame_obj)
        frames.append(frame)
    gif_obj = BytesIO()
    frames[0].save(gif_obj, format='GIF', save_all=True, append_images=frames, loop=0)
    if n > 1:
        n -= 1
        return split_test(gif_obj, n)
    return frame_test(gif_obj, 2.5)

def isurl(file_path):
    try:
        req = urllib.request.urlopen(file_path)
        status = req.getcode()
        if status == 200:
            return True
        else:
            return False
    except:
        return False

def check_gif(file_path):
    """Checks if used image is a gif or list of frames"""
    if isinstance(file_path, BytesIO):
        return
    elif (isfile(file_path)):
        file_ext = ''
        try:
            file_ext = os.path.splitext(file_path)[1]
        except:
            print("Please use a suitable file type.")
        assert file_ext == '.gif', 'Please use a GIF file.'
    elif (isurl(file_path)):
        file_ext = ''
        try:
            file_ext = os.path.splitext(file_path)[1]
        except:
            print("Please link a suitable file type.")
        assert file_ext == '.gif', 'Please link a GIF file.'
    else:
        file_ext = ''
        try:
            url_path = urllib.urlparse(file_path).path
            file_ext = os.path.splitext(url_path)[1]
        except:
            print("Problem grabbing image url.")
        assert file_ext == '.gif', 'Please use a GIF file.'

def test(file_path):
    """Runs both epilepsy tests in order of complexty"""
    e = frame_test(file_path)
    print(e)
    if (e == False):
        e = split_test(file_path)
        print(e)
    return e
