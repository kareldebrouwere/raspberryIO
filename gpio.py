'''
Created on 24-okt.-2015

@author: kareldebrouwere
'''
import RPi.GPIO as GPIO
import time

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4,True)
#    while True:
#        if (GPIO.input(3) == 0):
#            print("ButtonPressed")
#            time.sleep(1)
