from urllib.request import urlopen

from django.http import HttpResponse
from django.views import View

from .core.replacer import Replacer


class Proxy(View):

    def get(self, request, path=''):
        response = urlopen('https://habr.com/{}'.format(path))
        if request.is_ajax():
            return HttpResponse(content)

        info = response.info()
        content_type = info.get_content_type()
        content = response.read()

        if content_type != 'text/html':
            return HttpResponse(content)

        replacer = Replacer(content.decode('utf-8'))
        replaced = replacer.get_replaced()
        return HttpResponse(replaced)
