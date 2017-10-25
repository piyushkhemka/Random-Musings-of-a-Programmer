import cv2
import os
from PIL import Image

myimg = "image.jpg"
img = cv2.imread(myimg)
grayscale_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imwrite('image_grayscale.png', grayscale_img)
thresh, binarized_img = cv2.threshold(grayscale_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite('image_binarized.png', binarized_img)
