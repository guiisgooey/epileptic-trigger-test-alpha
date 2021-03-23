import os
from PIL import Image, ImageStat

def frame_test(file_path, threshold=5):
    """Converts gif/video into individual frames and compares frames to see if it is flashing"""
    e = False
    x = 0
    last = None
    check_gif(file_path)
    im = Image.open(file_path)
    x = im.n_frames
    file_starter = subpath(file_path)
    for n in range(x):
        if e == True:
            remove_file(f"{file_starter}_frame_{n-1}.png")
            break
        im.seek(n)
        im.save(f"{file_starter}_frame_{n}.png")
        frame = Image.open(f"{file_starter}_frame_{n}.png")
        remove_file(f"{file_starter}_frame_{n-1}.png")
        brightness = ImageStat.Stat(frame)
        current = brightness.rms[0]
        if last is not None:
            if (current > (last + last/threshold)) or (current < last - last/threshold):
                e = True
        if n == (x-1):
            remove_file(f"{file_starter}_frame_{n}.png")  
        last = brightness.rms[0]
    return e

def split_test(file_path, n=1):
    """Quarters gif n times and compares quartered frames using frame test"""
    e = False
    im = Image.open(file_path)
    w, h = im.size
    i = 1

    def remove_gif():
        remove_file(f"{os.path.splitext(file_path)[0]}_quarter_{i}.gif")

    if e == False:
        e = quarter_gif_test(file_path, 0, 0, w/2, h/2, i, n)
        remove_gif()
        i += 1
    if e == False:
        e = quarter_gif_test(file_path, w/2, h/2, w, h, i, n)
        remove_gif()
        i += 1
    if e == False:
        e = quarter_gif_test(file_path, w/2, 0, w, h/2, i, n)
        remove_gif()
        i += 1
    if e == False:
        e = quarter_gif_test(file_path, 0, h/2, w/2, h, i, n)
        remove_gif()
    return e

def remove_file(file_path):
    """Removes file if file exists"""
    if os.path.exists(file_path):
        os.remove(file_path)

def frames_to_gif(frames):
    pass

def gif_to_frames(file_path):
    pass

def check_gif(file_path):
    """Checks if used file is a gif"""
    file_ext = os.path.splitext(file_path)[1]
    assert file_ext == '.gif', 'Please use a GIF file.'
    

def subpath(file_path):
    """Returns subpath of path to be used for later files"""
    subpath = os.path.splitext(file_path)[0]
    return subpath


def quarter_gif_test(file_path, left, top, right, bottom, i, n=1):
    """Quarters gifs into quarter-gifs n times"""
    frames = []
    im = Image.open(file_path)
    x = im.n_frames
    file_starter = subpath(file_path)
    for j in range(x):
        im.seek(j)
        im.save(f"{file_starter}_{i}_{j}.png")
        frame = Image.open(f"{file_starter}_{i}_{j}.png")
        frame = frame.crop((left, top, right, bottom))
        frame.save(f"{file_starter}_quarter_{i}_frame_{j}.png")
        frame = Image.open(f"{file_starter}_quarter_{i}_frame_{j}.png")
        frames.append(frame)
        os.remove(f"{file_starter}_{i}_{j}.png")
    frames[0].save(f"{file_starter}_quarter_{i}.gif", save_all=True, append_images=frames, loop=0)
    for j in range(x):
        os.remove(f"{file_starter}_quarter_{i}_frame_{j}.png")
    if n > 1:
        n -= 1
        return split_test(f"{file_starter}_quarter_{i}.gif", n)
    return frame_test(f"{file_starter}_quarter_{i}.gif", 2.5)

def test(file_path):
    e = frame_test(file_path)
    if (e == False):
        e = split_test(file_path)
    return e
