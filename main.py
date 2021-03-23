from epilepsy_test import test
from epilepsy_test_video import video_frame_test

file_path = 'gifs/--YOUR_GIF_HERE.gif'
e = test(file_path)
print(e)

file_path2 = 'videos/--YOUR_VIDEO_HERE.mp4' #can be other video types besides mp4
e = video_frame_test(file_path2)
print(e)