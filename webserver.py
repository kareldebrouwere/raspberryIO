import cherrypy
import os

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

class Motor(object):
    def __init__(self):
        self.clockwise1 = """"<form method="get" action="clockwise1">
                            <button type="submit">Turn Clock Wise</button>
                            </form>"""
        self.clockwise2 = """"<form method="get" action="clockwise2">
                            <button type="submit">Turn Clock Wise Fast</button>
                            </form>"""
        self.anticlockwise = """"<form method="get" action="anticlockwise1">
                            <button type="submit">Turn anti Clock Wise</button>
                            </form>"""
        self.anticlockwise2 = """"<form method="get" action="clockwise2">
                                    <button type="submit">Turn anti Clock Fast</button>
                                    </form>"""
    @cherrypy.expose
    def index(self):
        pageHTML=HTML.format(clockwise1=self.clockwise1,clockwise2=self.clockwise2,anticlockwise=self.antioclockwise,anticlockwise2=self.antioclockwise2)
        return pageHTML


if __name__ == "__main__":
    config = os.path.join(os.path.dirname(__file__),'cherrypy.conf')
    cherrypy.quickstart(Motor(),config = config)
