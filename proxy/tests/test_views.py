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
