import os
import server
import unittest
import tempfile
from urlparse import urlparse
import json

class ServerTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, server.app.config['DATABASE'] = tempfile.mkstemp()
        server.app.testing = True
        self.app = server.app.test_client()
        # with server.app.app_context():
        #     server.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(server.app.config['DATABASE'])

    def test_get(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 405)

    def test_post_empty_body(self):
        rv = self.app.post('/', data={})
        self.assertEqual(rv.status_code, 401)

    def test_post_invalid_url(self):
        rv = self.app.post('/', data={'url': 'invalid_url'})
        self.assertEqual(rv.status_code, 401)

    def test_post_valid_url_and_get_redirect(self):
        rv = self.app.post('/', data={'url': 'http://www.google.com'})
        self.assertEqual(rv.status_code, 201)
        o = urlparse(json.loads(rv.data).get('shortened_url'))
        rv = self.app.get(o.path)
        self.assertEqual(rv.status_code, 301)


if __name__ == '__main__':
    unittest.main()
