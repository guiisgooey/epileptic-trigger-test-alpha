from epilepsy_test import frame_test, split_test, subpath, check_gif
from epilepsy_test_video import video_frame_test

#---Test that subpath helper method works---
assert subpath('gifs/test_case_1.gif') == 'gifs/test_case_1'
assert subpath('videos/coffee.mp4') == 'videos/coffee'

#---Test that flashing gifs are detected as flashing, non-flashing gifs are not---
assert frame_test('gifs/animation.gif') == False
assert frame_test('gifs/flashing.gif') == True
assert frame_test('gifs/flashing2.gif') == True

#---Test that fast moving gifs or flashing gifs with cancelling brightness are not detected ---
assert frame_test('gifs/pattern.gif') == False
assert frame_test('gifs/test_case_1.gif') == False
assert frame_test('gifs/test_case_2.gif') == False
assert frame_test('gifs/test_case_3.gif') == False
assert frame_test('gifs/test_case_4.gif') == False
assert frame_test('gifs/this nuts.gif') == False

#---Test that fast moving gifs or flashing gifs with cancelling brightness are detected---
assert split_test('gifs/test_case_1.gif') == True
assert split_test('gifs/test_case_2.gif', 2) == True
assert split_test('gifs/test_case_3.gif') == True
assert split_test('gifs/test_case_4.gif', 2) == True
assert split_test('gifs/this nuts.gif') == True

#---Test that gifs with cancelling brightness of higher complexity are not caught unless n is increased---
assert split_test('gifs/test_case_2.gif') == False
assert split_test('gifs/test_case_4.gif') == False

#---Test video frame test---
assert video_frame_test('videos/coffee.mp4') == False

print("--All tests completed successfully!--")