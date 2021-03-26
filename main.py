from epilepsy_test import test
from epilepsy_test_video import video_frame_test

file_path = 'gifs/test_case_1.gif'
e = test(file_path)

file_path2 = 'videos/flashing.mp4' #can be other video types besides mp4
e = video_frame_test(file_path2)
print(e)