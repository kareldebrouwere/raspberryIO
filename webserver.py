import cherrypy
import os
import motor

HMTL= HTML = """<html>
          <head></head>
          <body>
            <form>
              {clockwise1}
              {clockwise2}
              {anticlockwise}
              {anticlockwise2}
            </form>
          </body>
        </html>"""

class MotorWebServer(object):
    def __init__(self):
        self.clockwise1HTML = """<form method="get" action="clockwise1">
                            <button type="submit">Turn Clock Wise</button>
                            </form>"""
        self.clockwise2HTML = """<form method="get" action="clockwise2">
                            <button type="submit">Turn Clock Wise Fast</button>
                            </form>"""
        self.anticlockwiseHTML = """<form method="get" action="anticlockwise1">
                            <button type="submit">Turn anti Clock Wise</button>
                            </form>"""
        self.anticlockwise2HTML = """<form method="get" action="clockwise2">
                                    <button type="submit">Turn anti Clock Fast</button>
                                    </form>"""
    @cherrypy.expose
    def index(self):
        pageHTML=HTML.format(clockwise1=self.clockwise1HTML,clockwise2=self.clockwise2HTML,anticlockwise=self.anticlockwiseHTML,anticlockwise2=self.anticlockwise2HTML)
        #print (pageHTML)
        return pageHTML


    @cherrypy.expose
    def clockwise1(self):
        print("the clockwise1 method start")
        myMotor = motor.Motor()
        myMotor.turnClockWise()

if __name__ == "__main__":
    config = os.path.join(os.path.dirname(__file__),'cherrypy.conf')
    cherrypy.quickstart(MotorWebServer(),config = config)
