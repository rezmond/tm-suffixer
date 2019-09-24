# -*- coding: utf-8 -*-
# author: makarov
import re

from typing import Iterable, Set
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from bs4.element import Tag


def iterate_nodes(tree: BeautifulSoup) -> Iterable:
    def run(node):
        yield node
        children = getattr(node, 'children', [])
        for sub in children:
            yield from run(sub)

    return run(tree)


def replace_href(anchor: Tag, replacing_hosts: Set[str]) -> None:
    href = anchor.attrs.get('href')

    if href is None:
        return

    src_url = urlparse(href)
    host = src_url.netloc.split(':')[0]
    if host not in replacing_hosts:
        return

    replaced = src_url._replace(scheme='', netloc='')
    anchor.attrs['href'] = replaced.geturl()


def replace_text(src: str, word_length):
    pattern = r'(\b[\w]{%s}\b)' % word_length
    replaced = re.sub(pattern, r'\1™', src)
    return replaced
