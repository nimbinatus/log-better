import cherrypy


class Root(object):
    @cherrypy.expose
    def index(self):
        return """<html>
        <head></head>
        <body>
            <h1>Hello, world!</h1>
            <h2>Basic Log Line</h2>
            <form method="get" action="logme">
                <input type="text" value="nothing" name="incoming" />
                <button type="submit">Send</button>
            </form>
        </body>
        </html>"""


class LogEndpoint(object):
    @cherrypy.expose
    def logme(self, incoming='Nothing'):
        cherrypy.log('Logged: {}'.format(str(incoming)))
        return '{} is what I received.'.format(str(incoming))

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def jsonin(self):
        data = cherrypy.request.json
        cherrypy.log("{} I received this JSON object".format(data))
        return "I received a log line! It was {}".format(data)


if __name__ == '__main__':
    cherrypy.quickstart(Root(), '/')
