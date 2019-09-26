import cherrypy
import os
import simplejson as json


class Root(object):
    @cherrypy.expose
    def index(self):
        return open('/web/index.js')


@cherrypy.expose
class HealthCheck(object):
    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return "I'm alive!"


@cherrypy.expose
class LogEndpoint(object):
    @cherrypy.tools.accept(media='text/plain')
    @cherrypy.tools.json_out()
    def POST(self, incoming='nothing'):
        if cherrypy.request:
            incoming = cherrypy.request.body.read().decode('utf-8')
        cherrypy.log('LOG: Logged: {}'.format(incoming))
        message = 'LOG: {}'.format(str(incoming))
        return {'body': message}


@cherrypy.expose
class JsonLogEndpoint(object):
    @cherrypy.tools.accept(media='application/json')
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        returnstring = []
        try:
            dataSet = cherrypy.request.json
            print(dataSet)
            for elem in dataSet:
                cherrypy.log("Logged: {} as {}".format(elem, dataSet[elem]))
                returnstring.append("Log: {} as {}".format(elem, dataSet[elem]))
            print(returnstring)
            cherrypy.response.body = '\n'.join(returnstring).encode('utf-8')
            cherrypy.response.status = 200
        except Exception as err:
            print(err)
            cherrypy.response.status = 400
            cherrypy.response.body = "{}".format(err)
        finally:
            return cherrypy.response.body


if __name__ == '__main__':
    env = os.environ.get('APP_ENV', 'local')
    server_type = os.environ.get('APP_TYPE', 'api')
    base_config = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain'), ('Content-Type', 'application/json')]
        }
    }

    cherrypy.tree.mount(Root(), '/', base_config)
    cherrypy.tree.mount(HealthCheck(), '/health', base_config)
    cherrypy.tree.mount(LogEndpoint(), '/basic', base_config)
    cherrypy.tree.mount(JsonLogEndpoint(), '/api', base_config)

    cherrypy.engine.start()
    cherrypy.engine.block()
