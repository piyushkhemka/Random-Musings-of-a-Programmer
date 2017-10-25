# Captures every frame of an mp4 video.

import cv2
video_obj = cv2.VideoCapture('test.mp4')
success,image = video_obj.read()
count = 0
success = True
while success:
  success,image = video_obj.read()
  print('Read a new frame: ', success)
  cv2.imwrite("%d.jpg" % count, image)     # save frame as JPEG file
  count += 1
