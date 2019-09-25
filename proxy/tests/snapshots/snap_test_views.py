# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['ViewsTestCases::test_root 1'] = '<html><body>sixsix™</body></html>'

snapshots['ViewsTestCases::test_doctype 1'] = '''<!DOCTYPE html>
<html><body>test</body></html>'''
