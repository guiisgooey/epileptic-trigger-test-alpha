from epilepsy_test import test
from epilepsy_test_video import video_frame_test

file_path = 'https://media1.giphy.com/media/xT0xeuOy2Fcl9vDGiA/giphy.gif'
e = test(file_path)
print('------------------')
file_path2 = 'videos/flashing.mp4' #can be other video types besides mp4
e = video_frame_test(file_path2)
print(e)