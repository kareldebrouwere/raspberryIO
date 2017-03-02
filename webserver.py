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
        self.clockwise1HTML = """<form method="get" action="start">
                            <button type="submit">Turn Clock Wise</button>
                            </form>"""
        self.clockwise2HTML = """<form method="get" action="stop">
                            <button type="submit">Turn Clock Wise Fast</button>
                            </form>"""
        self.anticlockwiseHTML = """<form method="get" action="start">
                            <button type="submit">Turn anti Clock Wise</button>
                            </form>"""
        self.anticlockwise2HTML = """<form method="get" action="start">
                                    <button type="submit">Turn anti Clock Fast</button>
                                    </form>"""
    @cherrypy.expose
    def index(self):
        pageHTML=HTML.format(clockwise1=self.clockwise1HTML,clockwise2=self.clockwise2HTML,anticlockwise=self.anticlockwiseHTML,anticlockwise2=self.anticlockwise2HTML)
        print (pageHTML)
        return pageHTML


    @cherrypy.expose
    def start(self):
        print("the clockwise1 method start")
        self.myMotor = motor.Motor()
        self.myMotor.run()
        return self.index()

    @cherrypy.expose
    def stop(self):
        self.myMotor.stop()
        return self.index()

if __name__ == "__main__":
    config = os.path.join(os.path.dirname(__file__),'cherrypy.conf')
    cherrypy.quickstart(MotorWebServer(),config = config)
