from PIL import ImageGrab
import numpy as np
import cv2
import tensorflow as tf
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
model = tf.keras.models.load_model('model.h5')

while True:
	# PUT GAME SCREEN IN THIS AREA
	printscreen =  np.array(ImageGrab.grab(bbox=(30,200,453,740)))

	img = cv2.Canny(printscreen,200,300)
	img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

	img = cv2.resize(img, (300, 300), interpolation = cv2.INTER_AREA)
	img = np.expand_dims(img, axis=0)
	n = model.predict(img)
	k = np.argmax(n[0])

	if k == 0 or k == 4 or k == 7 or k == 8:
		keyboard.press(Key.up)
		keyboard.release(Key.up)
		print("JUMP")
	elif k == 1 or k == 9:
		keyboard.press(Key.left)
		keyboard.release(Key.left)
		print("LEFT")
	elif k == 2 or k == 3 or k == 10:
		keyboard.press(Key.right)
		keyboard.release(Key.right)
		print("RIGHT")
	elif k == 5:
		print("NOTHING")
	elif k == 6:
		keyboard.press(Key.down)
		keyboard.release(Key.down)
		print("ROLL")

	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break
