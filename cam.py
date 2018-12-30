from picamera import PiCamera
from time import sleep,time

cam = PiCamera()

cam.capture("/sm_farming/{}.jpg".format(time()))  
