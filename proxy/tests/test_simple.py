from snapshottest import TestCase

from proxy.core.replacer import Replacer
from proxy.core.utils import replace_text


class SimpleTestCases(TestCase):

    def test_replace(self):
        self.assertMatchSnapshot(replace_text('word longword Sixsix', 6))

    def test_silent_no_existed_href(self):
        replacer = Replacer(
            '<body><a class="anchor-class"> anchor text </a></body>')
        self.assertMatchSnapshot(replacer.get_replaced())

    def test_replace_certain_host(self):
        replacer = Replacer(
            '<body><a href="https://habr.com/one/two"> anchor text </a></body>')
        self.assertMatchSnapshot(replacer.get_replaced())
        replacer = Replacer(
            '<body><a href="https://medium.com/one/two"> anchor text </a></body>')
        self.assertMatchSnapshot(replacer.get_replaced())

    def test_replace_html(self):
        replacer = Replacer("""<html>
            <body>
                body text
                <a
                    class="anchor-class"
                    href="https://test.com/link/to/external/resource/sixsix"
                >
                    anchor text
                </a>
                <a
                    class="anchor-class"
                    href="https://habr.com/link/to/external/resource/sixsix"
                >
                    anchor text
                </a>
                longword
                Sixsix
            </body>
        </html>""")
        self.assertMatchSnapshot(replacer.get_replaced())
