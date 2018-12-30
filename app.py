import os,time
import RPi.GPIO as GPIO
import serial

GPIO.setmode(GPIO.BOARD)

port = serial.Serial("/dev/ttyAMA0",baudrate=9600,timeout=1)
