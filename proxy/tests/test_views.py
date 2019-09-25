from unittest.mock import patch

from django.test import TestCase, Client
from snapshottest import TestCase as SnapshotTestCase


def patch_response(response):
    return patch(
        'proxy.views.urlopen', **{
            'return_value.read.return_value': response
        })


class ViewsTestCases(TestCase, SnapshotTestCase):

    def test_root(self):
        client = Client()

        with patch_response(b'<html><body>sixsix</body></html>'):
            response = client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertMatchSnapshot(response.content.decode('utf-8'))

    def test_doctype(self):
        client = Client()

        with patch_response(b'<!DOCTYPE html><html><body>test</body></html>'):
            response = client.get('/test')

        self.assertEqual(response.status_code, 200)
        self.assertMatchSnapshot(response.content.decode('utf-8'))

    def test_scripts(self):
        client = Client()

        page = b'''
        <!DOCTYPE html>
        <html>
            <body>
                should have the mark
                <script>should not have the mark</script>
            </body>
        </html>'
        '''

        with patch_response(page):
            response = client.get('/test')

        self.assertEqual(response.status_code, 200)
        self.assertMatchSnapshot(response.content.decode('utf-8'))

    def test_comments(self):
        client = Client()

        page = b'''
        <!DOCTYPE html>
        <html>
            <body>
                should have the mark
                <!--Should not be changed-->
                <b>
                    <!--Should not be changed too-->
                </b>
            </body>
        </html>'
        '''

        with patch_response(page):
            response = client.get('/test')

        self.assertEqual(response.status_code, 200)
        self.assertMatchSnapshot(response.content.decode('utf-8'))
