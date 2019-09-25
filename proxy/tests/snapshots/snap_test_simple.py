# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['SimpleTestCases::test_replace 1'] = 'word longword Sixsix™'

snapshots['SimpleTestCases::test_replace_certain_host 1'] = '<body><a href="/one/two"> anchor™ text </a></body>'

snapshots['SimpleTestCases::test_replace_certain_host 2'] = '<body><a href="https://medium.com/one/two"> anchor™ text </a></body>'

snapshots['SimpleTestCases::test_replace_html 1'] = '''<html>
<body>
                body text
                <a class="anchor-class" href="https://test.com/link/to/external/resource/sixsix">
                    anchor™ text
                </a>
<a class="anchor-class" href="/link/to/external/resource/sixsix">
                    anchor™ text
                </a>
                longword
                Sixsix™
            </body>
</html>'''

snapshots['SimpleTestCases::test_silent_no_existed_href 1'] = '<body><a class="anchor-class"> anchor™ text </a></body>'
