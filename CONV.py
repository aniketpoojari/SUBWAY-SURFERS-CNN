CONVERT ALL DATASET IMAGES TO GRAYSCALE AND APPLY CANNY EDGE DETECTION

import cv2
import os

cwd = os.getcwd() + "/DATA/TESTING/"


for f in os.listdir(cwd):
	for i in os.listdir(cwd + f):
		img = cv2.imread(cwd + f + "/" + i, cv2.IMREAD_GRAYSCALE)
		img = cv2.Canny(img,200,300)
		cv2.imwrite(cwd + f + "/" + i, img)
	
cv2.waitKey(0)
cv2.destroyAllWindows()
