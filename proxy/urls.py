# -*- coding: utf-8 -*-

from django.urls import path

from .views import Proxy

urlpatterns = [
    path('<path:path>', Proxy.as_view()),
]
