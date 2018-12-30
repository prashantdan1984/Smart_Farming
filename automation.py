from time import sleep
import RPi.GPIO as GPIO
import os


GPIO.setwarnings(False)

port ={
        1:7,
        2:11,
        3:12,
        4:13,
        5:15,
        6:16,
        7:18,
        8:22,
        9:29,
        10:31,
        11:32,
        12:33,
        13:35,
        14:36,
        15:37,
        16:38
      }


GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)



def write(pin,out):
    if pin:
        if out:
            GPIO.output(port[pin],GPIO.LOW)            
        else:
            GPIO.output(port[pin],GPIO.HIGH)
