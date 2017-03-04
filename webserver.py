import cherrypy
import os
import motor
import logging

HMTL= HTML = """<html>
          <head></head>
          <body>
              {button1}
              {button2}
              {direction}
          </body>
        </html>"""

class MotorWebServer(object):
    def __init__(self):

        self.startHTML = """<form method="get" action="start">
                            <button type="submit">Make it Turn</button>
                            <input type="text" name="speed">
                            <input type="radio" name="direction" value="clock"> Clockwise<br>
                            <input type="radio" name="direction" value="anti clock"> Anti Clockwise<br>
                            </form>"""
        self.stopHTML = """<form method="get" action="stop">
                            <button type="submit">Stop</button>
                        </form>"""

        self.myMotor = motor.Motor()

        logging.basicConfig(filename='webserver.log',level=logging.INFO)

    @cherrypy.expose
    def index(self):
        pageHTML=HTML.format(button1=self.startHTML,button2=self.stopHTML)
        #print (pageHTML)
        return pageHTML

    @cherrypy.expose
    def start(self,speed=10,direction="clock"):
        logging.info("method start with speed="+str(speed)+ " and direction= "+str(direction))
        print("Direction: "+direction)
        if direction == "clock":
            self.myMotor.StepDir = 1
        elif direction == "anticlock":
            self.myMotor.StepDir = -1
        self.myMotor.runningStatus=True
        try:
            self.myMotor.WaitTime = float(0.0001/int(speed))
        except:
            print("Speed= " + str(speed))
        self.myMotor.run()
        return self.index()

    @cherrypy.expose
    def stop(self):
        self.myMotor.runningStatus=False
        return self.index()

if __name__ == "__main__":
    config = os.path.join(os.path.dirname(__file__),'cherrypy.conf')
    cherrypy.quickstart(MotorWebServer(),config = config)
