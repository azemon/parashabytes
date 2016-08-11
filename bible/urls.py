"""eichaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.decorators.cache import cache_page

from .views import TextRetrieveView, NormalizeLocationView

app_name = 'bible'

urlpatterns = [
    url(
        regex=r'api/v1/texts/(?P<reference>.+)$',
        view=cache_page(60 * 60 * 24 * 7)(TextRetrieveView), # cache for a week
        name='texts',
    ),
    url(
        regex=r'api/v1/normalize/(?P<reference>.+)$',
        view=cache_page(60 * 60 * 24 * 7)(NormalizeLocationView), # cache for a week
        name='normalize',
    ),
]
