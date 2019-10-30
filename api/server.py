import cherrypy
import cherrypy_cors
import os
# import simplejson as json
import structlog

cherrypy_cors.install()
logger = structlog.get_logger()


@cherrypy.expose
class Root(object):
    # @cherrypy.expose
    def GET(self):
        raise cherrypy.HTTPRedirect("https://logbetter-web.nimbinatus.com/", status=302)


@cherrypy.expose
class HealthCheck(object):
    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return

@cherrypy.expose
class LogEndpoint(object):
    def OPTIONS(self):
        return

    @cherrypy.tools.accept(media='text/plain')
    @cherrypy.tools.json_out()
    def POST(self):
        log = logger.bind(
            server_protocol=cherrypy.request.server_protocol,
            scheme=cherrypy.request.scheme,
            remote=cherrypy.request.remote,
            local=cherrypy.request.local
        )
        if cherrypy.request:
            incoming = cherrypy.request.body.read().decode('utf-8')
        log.msg('LOG: Data is {}'.format(incoming), data=incoming)
        message = 'LOG: {}'.format(str(incoming))
        return {'body': message}


@cherrypy.expose
class JsonLogEndpoint(object):
    def OPTIONS(self):
        return

    @cherrypy.tools.accept(media='application/json')
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        log = logger.bind(
            user_agent="UNKNOWN",
            peer_ip="0.0.0.0"
        )
        returnstring = []
        try:
            dataSet = cherrypy.request.json
            for elem in dataSet:
                log.msg("LOG: Data {} as {}".format(elem, dataSet[elem]))
                returnstring.append("Log: {} as {}".format(elem, dataSet[elem]))
            cherrypy.response.body = '\n'.join(returnstring).encode('utf-8')
            cherrypy.response.status = 200
        except Exception as err:
            cherrypy.response.status = 400
            cherrypy.response.body = "{}".format(err)
        finally:
            log.msg("RES: {} with {}".format(cherrypy.response.status, cherrypy.response.body))
            return cherrypy.response.body


if __name__ == '__main__':
    env = os.environ.get('APP_ENV', 'local')
    server_type = os.environ.get('APP_TYPE', 'api')
    origins = ['https://logbetter-web.nimbinatus.com', 'localhost:8081']
    base_config = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [
                ('Content-Type', 'text/plain'),
                ('Content-Type', 'application/json'),
                ('Access-Control-Allow-Origin', 'https://logbetter-web.nimbinatus.com'),
                ('Access-Control-Allow-Methods', 'POST, GET, OPTIONS'),
                ('Access-Control-Allow-Headers', 'Content-Type')
                # ('Access-Control-Allow-Origin', 'localhost:8081')
            ],
            'cors.expose.on': True,
            'cors.expose.origins': origins,
            'cors.preflight.origins': origins,
            'log.screen': True
        }
    }

    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.tree.mount(Root(), '/', base_config)
    cherrypy.tree.mount(HealthCheck(), '/health', base_config)
    cherrypy.tree.mount(LogEndpoint(), '/basic', base_config)
    cherrypy.tree.mount(JsonLogEndpoint(), '/api', base_config)

    cherrypy.engine.start()
    cherrypy.engine.block()
