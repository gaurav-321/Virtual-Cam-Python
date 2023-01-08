import time
from glob import glob
import cv2
import keyboard
import pyvirtualcam

vid = glob("input_vid/*")[0]
cap = cv2.VideoCapture(vid)
send = 0
FPS = int(cap.get(cv2.CAP_PROP_FPS))


def wait():
    s_time = time.time()
    while time.time() - s_time < 1 / FPS:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                print('You Pressed A Key!')
                return True  # finishing the loop
        except:
            break
    return False


with pyvirtualcam.Camera(width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                         fps=FPS) as cam:
    while cap.isOpened():
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cam.send(frame)
        if wait():
            cap.release()
            exit()
        cam.sleep_until_next_frame()
        cam.sleep_until_next_frame()
