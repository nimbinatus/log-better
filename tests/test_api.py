#! /usr/bin/env python

# Adapted from https://bitbucket.org/Lawouach/cherrypy-recipes/src/tip/testing/unit/serverless/cptestcase.py

import cherrypy
import cherrypy.lib.httputil
import json
import unittest
import urllib.parse

from io import BytesIO

from context import api as localapi


local = cherrypy.lib.httputil.Host('localhost', 50000)
remote = cherrypy.lib.httputil.Host('localhost', 50001)

__all__ = ['BaseTestCase']


def setup1(app, mntpnt):
    cherrypy.config.update({'environment': 'test_suite'})
    cherrypy.server.unsubscribe()
    cherrypy.tree.mount(app, mntpnt)
    cherrypy.engine.start()


class BaseTestCase(unittest.TestCase):
    def request(self, path='/', method='GET', app_path='', scheme='http',
                proto='HTTP/1.1', data=None, headers=None, ctype=None, **kwargs):
        h1 = [{'Host': '127.0.0.1'}]
        qs = None
        fd = None

        if headers is not None:
            h1.update(headers)

        if method in ['POST', 'PUT'] and not data:
            data = urllib.parse.urlencode(kwargs)
            kwargs = None
            h1.append({'content-type': 'application/x-www-form-urlencoded'})

        if method in ['POST', 'PUT'] and ctype:
            h1.append({'content-type': '{}'.format(ctype)})

        if kwargs:
            qs = urllib.parse.urlencode(kwargs)

        if data is not None:
            h1.append({'content-length': '%d' % len(data)})
            fd = BytesIO(data.encode())

        app = cherrypy.tree.apps.get(app_path)
        if not app:
            raise AssertionError("No application mounted at {}".format(app_path))

        app.release_serving()

        request, response = app.get_serving(local, remote, scheme, proto)
        h = []
        try:
            for elem in h1:
                for key, value in elem.items():
                    h.append((key, value))
            response = request.run(method, path, qs, proto, h, fd)
        finally:
            if fd:
                fd.close()
                fd = None

        if response.output_status.startswith(b'500'):
            raise AssertionError('Unexpected error: {}'.format(cherrypy.serving.request.error_response))

        response.collapse_body()
        return response


class TestRoot(BaseTestCase):
    def setUp(self):
        setup1(localapi.Root(), '/')

    def test_root(self):
        res = self.request(path='/')
        self.assertEqual(res.output_status, b'200 OK')
        self.assertEqual(res.body, [b'hello world'])

    def tearDown(self):
        cherrypy.engine.exit()


class TestHealth(BaseTestCase):
    def setUp(self):
        setup1(localapi.HealthCheck(), '/')

    def test_health(self):
        res = self.request(path='/')
        self.assertEqual(res.output_status, b'200 OK')
        self.assertEqual(res.body, [b'OK'])

    def tearDown(self):
        cherrypy.engine.exit()


class TestLog(BaseTestCase):
    def setUp(self):
        setup1(localapi.LogEndpoint(), '/')

    def test_plain(self):
        res = self.request(path='/', data='testing', method='POST', ctype='text/plain')
        self.assertEqual(res.output_status, b'200 OK')
        self.assertEqual(res.body, [b'LOG: testing'])

    def tearDown(self):
        cherrypy.engine.exit()


class TestJSON(BaseTestCase):
    def setUp(self):
        setup1(localapi.JsonLogEndpoint(), '/')

    def test_json(self):
        body = json.dumps({'key 1': 'value 1', 'key 2': 'value 2'})
        res = self.request(path='/', method='POST', data=body, ctype='application/json')
        self.assertEqual(res.body[0], b'value 1')

    def tearDown(self):
        cherrypy.engine.exit()


if __name__ == '__main__':
    unittest.main()
