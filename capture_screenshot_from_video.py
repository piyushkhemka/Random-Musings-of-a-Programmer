import cv2
import math
import os

videoFile = "test.mp4"
imagesFolder = "images"
if not os.path.exists(imagesFolder):
    os.makedirs(imagesFolder)

video_obj = cv2.Videovideo_objture(videoFile)
frameRate = video_obj.get(5) #frame rate
while(video_obj.isOpened()):
    frameId = video_obj.get(1) #current frame number
    ret, frame = video_obj.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename = imagesFolder + "/image_" +  str(int(frameId)) + ".jpg"
        cv2.imwrite(filename, frame)
video_obj.release()
print "Done!"
