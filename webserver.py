import cherrypy
import os
import motor
import logging

HMTL= HTML = """<html>
          <head></head>
          <body>
              {button1}
              {button2}
              {quarter}
          </body>
        </html>"""

class MotorWebServer(object):
    def __init__(self):

        self.startHTML = """<form method="get" action="start">

                            Speed <input type="text" name="speed"><br>
                            <input type="radio" name="direction" value="clock"> Clockwise<br>
                            <input type="radio" name="direction" value="anticlock"> Anti Clockwise<br>
                            <button type="submit">Make it Turn</button><br>
                            </form>"""
        self.stopHTML = """<form method="get" action="stop">
                            <button type="submit">Stop</button><br>
                        </form>"""
        self.quarter = """<form method="get" action="quarter">
                            <button type="submit">Quarter</button><br>
                        </form>"""

        self.myMotor = motor.Motor()

        logging.basicConfig(filename='webserver.log',level=logging.INFO)

    @cherrypy.expose
    def index(self):
        pageHTML=HTML.format(button1=self.startHTML,button2=self.stopHTML,quarter=self.quarter)
        #print (pageHTML)
        return pageHTML

    @cherrypy.expose
    def start(self,speed=10,direction="clock"):
        logging.info("method start with speed="+str(speed)+ " and direction= "+str(direction))
        print("Direction: "+direction)
        if str(direction) == "clock":
            self.myMotor.StepDir = 1
        elif str(direction) == "anticlock":
            logging.info("Setting direction to anticlock wise")
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

    @cherrypy.expose
    def quarter(self):
        self.myMotor.quarterturn()
        return self.index()

if __name__ == "__main__":
    config = os.path.join(os.path.dirname(__file__),'cherrypy.conf')
    cherrypy.quickstart(MotorWebServer(),config = config)
