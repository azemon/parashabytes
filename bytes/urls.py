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
from django.views.generic import TemplateView

from .views import parasha_detail, parasha_edit, parasha_list, portion_edit, portion_list

app_name = 'bytes'

urlpatterns = [
    url(r'^parasha/$', parasha_list, name='parasha'),
    url(r'^parasha/(?P<pk>[0-9]+)/$', parasha_detail, name='parasha_detail'),
    url(r'^parasha/(?P<pk>[0-9]+)/edit/$', parasha_edit, name='parasha_edit'),

    url(r'^portion/$', portion_list, name='portion'),
    #url(r'^portion/(?P<pk>[0-9]+)/$', portion_detail, name='portion_detail'),
    url(r'^portion/(?P<pk>[0-9]+)/edit/$', portion_edit, name='portion_edit'),

    url(r'^$', TemplateView.as_view(template_name='bytes/index.html'), name='index'),
]
