# -*- coding: utf-8 -*-
# author: makarov

from bs4 import BeautifulSoup
from bs4.element import NavigableString

from .utils import iterate_nodes, replace_href, replace_text


class Replacer:

    words_length = 6
    replacing_hosts = {
        'habr.com',
        'habrahabr.ru',
    }

    def __init__(self, src: str) -> None:
        super(Replacer, self).__init__()
        self._src = BeautifulSoup(src, features='html.parser')

    def get_replaced(self) -> str:
        for node in iterate_nodes(self._src):
            if isinstance(node, NavigableString):
                node.string.replace_with(
                    replace_text(node.string, self.words_length))

            elif node.name == 'a':
                replace_href(node, self.replacing_hosts)

        return str(self._src)
