
import os
import cv2
import matplotlib.pyplot as plt
from src.config import SAVE_LOCATION

import cv2
import os

image_folder = SAVE_LOCATION
video_name = 'video.avi'

def _key(img) :
    return int(img.split(".")[0])

images = sorted([img for img in os.listdir(image_folder)], key = _key)
print(images)
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
video = cv2.VideoWriter(video_name, 0, 10, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

#cv2.destroyAllWindows()
video.release()
plt.close()