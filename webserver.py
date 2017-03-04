import cherrypy
import os
import motor

HMTL= HTML = """<html>
          <head></head>
          <body>
              {button1}
              {button2}
          </body>
        </html>"""

class MotorWebServer(object):
    def __init__(self):

        self.startHTML = """<form method="get" action="start">
                            <button type="submit">Turn anti Clock Wise</button>
                            <input type="text" name="speed">
                            </form>"""
        self.stopHTML = """<form method="get" action="stop">
                            <button type="submit">Stop</button>
                            <input type="text" name="speed">
                            </form>"""
        self.myMotor = motor.Motor()

    @cherrypy.expose
    def index(self):
        pageHTML=HTML.format(button1=self.startHTML,button2=self.stopHTML)
        print (pageHTML)
        return pageHTML

    @cherrypy.expose
    def start(self,speed):
        print("the clockwise1 method start")
        self.myMotor.WaitTime = speed/10000
        self.myMotor.run()
        return """<html><head>RUNNING</head></html>"""

    @cherrypy.expose
    def stop(self):
        self.myMotor.runningStatus=False
        return """<html><head>STOPPED</head></html>"""

if __name__ == "__main__":
    config = os.path.join(os.path.dirname(__file__),'cherrypy.conf')
    cherrypy.quickstart(MotorWebServer(),config = config)
