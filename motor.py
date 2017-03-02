#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO


class Motor(object):

    def __init__(self):
        # Use BCM GPIO references
        # instead of physical pin numbers
        GPIO.setmode(GPIO.BCM)
 
        # Define GPIO signals to use
        # Physical pins 11,15,16,18
        # GPIO17,GPIO22,GPIO23,GPIO24
        self.StepPins = [17,22,23,24]

        # Set all pins as output
        for pin in self.StepPins:
            print ("Setup pins")
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, False)

        # Define advanced sequence
        # as shown in manufacturers datasheet
        self.Seq = [[1,0,0,1],
               [1,0,0,0],
               [1,1,0,0],
               [0,1,0,0],
               [0,1,1,0],
               [0,0,1,0],
               [0,0,1,1],
               [0,0,0,1]]

        self.StepCount = len(Seq)
        self.StepDir = 1 # Set to 1 or 2 for clockwise
                    # Set to -1 or -2 for anti-clockwise
 
        self.WaitTime = 10/float(1000)
 
        # Initialise variables
        StepCounter = 0
        print ("Motor has been created")

    def turnClockWise(self):
        print ("starting the motor")
        while True:

          print (self.StepCounter)
          print (self.Seq[self.StepCounter])
          for pin in range(0,4):
            xpin=self.StepPins[pin]# Get GPIO
            if self.Seq[self.StepCounter][pin]!=0:
              print (" Enable GPIO %i" %(xpin))
              GPIO.output(xpin, True)
            else:
              GPIO.output(xpin, False)

          self.StepCounter += self.StepDir

          # If we reach the end of the sequence
          # start again
          if (self.StepCounter>=self.StepCount):
            self.StepCounter = 0
          if (self.StepCounter<0):
            self.StepCounter = self.StepCount+self.StepDir

          # Wait before moving on
          time.sleep(self.WaitTime/50)