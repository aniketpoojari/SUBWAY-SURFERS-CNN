import numpy as np
from PIL import ImageGrab
import cv2
import keyboard
from datetime import datetime

FILE = "DATA/NEW-DATA/"
record = False

while(True):
    
    # KEEP THE GAME WINDOW IN THIS REGION
    printscreen =  np.array(ImageGrab.grab(bbox=(30,200,453,740)))
    img = cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB)
    cv2.imshow('window', img)
    
    # PRESS r TO STOP OR START RECORDING DATA
    if keyboard.is_pressed('r'):
        if record == True:
            print("STOPPED RECORDING")
            record = False
        else:
            print("RECORDING")
            record = True
        while keyboard.is_pressed("r"):
            pass

    # WHEN KEY IS PRESSED THEN DATA IS RECORDED
    if record == True:
        if keyboard.is_pressed('up'):
            print("JUMP")
            cv2.imwrite(FILE + str(datetime.timestamp(datetime.now())) + ".jpg", img)
            while keyboard.is_pressed("up"):
                pass
        elif keyboard.is_pressed('down'):
            print("ROLL")
            cv2.imwrite(FILE + str(datetime.timestamp(datetime.now())) + ".jpg", img)
            while keyboard.is_pressed("down"):
                pass
        elif keyboard.is_pressed('left'):
            print("left")
            cv2.imwrite(FILE + str(datetime.timestamp(datetime.now())) + ".jpg", img)
            while keyboard.is_pressed("left"):
                pass
        elif keyboard.is_pressed('right'):
            print("right")
            cv2.imwrite(FILE + str(datetime.timestamp(datetime.now())) + ".jpg", img)
            while keyboard.is_pressed("right"):
                pass
        elif keyboard.is_pressed('n'):
            print("nothing")
            cv2.imwrite(FILE + str(datetime.timestamp(datetime.now())) + ".jpg", img)
            while keyboard.is_pressed('s'):
                pass

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
 
