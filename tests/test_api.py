#! /usr/bin/env python

import unittest
from context import api as localapi


class TestHealth(unittest.TestCase):
    def test_health(self):
        res = localapi.HealthCheck.GET(self)
        self.assertEqual(res, 'OK')


class TestLog(unittest.TestCase):
    def test_plain(self):
        res = localapi.LogEndpoint.POST(self, incoming='testing')
        self.assertEqual(res, 'testing')


class TestJSON(unittest.TestCase):
    def test_json(self):
        pass


if __name__ == '__main__':
    unittest.main()
