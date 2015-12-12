'''
Created on 24-okt.-2015

@author: kareldebrouwere
'''

import cherrypy
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4,GPIO.OUT)



HTML = """<html>
          <head></head>
          <body>
            <form method="get" action="start">
              {button}
              <button type="submit">Start</button>
            </form>
            <form method="get" action="{actionForRed}">
              <button type="submit">Toggle red LED</button>
            </form>
          </body>
        </html>"""

class Test(object):
    
    def __init__(self):
        self.buttonRed =  """<img src="/static/buttonRed.jpg" height="100" width="100">"""
        self.buttonGreen =  """<img src="/static/buttonGreen.png" height="100" width="100">"""
        self.buttonGrey =  """<img src="/static/buttonGrey.jpg" height="100" width="100">"""
    
    @cherrypy.expose
    def index(self):
        return HTML.format(button=self.buttonGrey,actionForRed="turnRedOn")
    
    @cherrypy.expose
    def start(self):
        self.index()
        while True:
            if (GPIO.input(2) == 0):
                return HTML.format(button=self.buttonRed)
            if (GPIO.input(3) == 0):
                return HTML.format(button=self.buttonGreen)
            time.sleep(0.1)
    
    @cherrypy.expose        
    def turnRedOn(self):
        GPIO.output(4,True)
        return HTML.format(button=self.buttonGrey,actionForRed="turnRedOff")
    
    @cherrypy.expose        
    def turnRedOff(self):
        GPIO.output(4,False)
        return HTML.format(button=self.buttonGrey,actionForRed="turnRedOn")
    
if __name__ == "__main__":
    GPIO.output(4,False)
    config = os.path.join(os.path.dirname(__file__),'cherrypy.conf')
    cherrypy.quickstart(Test(),config = config)