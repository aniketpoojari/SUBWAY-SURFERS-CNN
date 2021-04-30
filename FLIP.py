# FLIP ALL DATASET IMAGES TO GET MORE DATA

import cv2
import os

getcwd = os.getcwd() + "/DATA/NEW-DATA/"

for f in os.listdir(getcwd):
	img = cv2.imread(getcwd + f)
	flipHorizontal = cv2.flip(img, 1)
	name = f.split(".jpg")[0][::-1] + ".jpg"
	cv2.imwrite(getcwd + name, flipHorizontal)

cv2.waitKey(0)
cv2.destroyAllWindows()