from urllib.request import urlopen

from django.http import HttpResponse
from django.views import View

from .core.replacer import Replacer


class Proxy(View):

    def get(self, request, path=''):
        content = urlopen('https://habr.com/{}'.format(path)).read()
        replacer = Replacer(content.decode('utf-8'))
        replaced = replacer.get_replaced()
        return HttpResponse(replaced)
