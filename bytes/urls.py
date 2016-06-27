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

from .views_location import LocationCreateView, LocationListView
from .views_parasha import ParashaDetailView, ParashaListView, ParashaUpdateView
from .views_reading import ReadingCreateView, ReadingListView, ReadingUpdateView
from .views_word import WordCreateView, WordDetailView, WordListView, WordUpdateView

app_name = 'bytes'

urlpatterns = [
    url(
        regex=r'location/$',
        view=LocationListView.as_view(),
        name='location'
    ),
    url(
        regex=r'location/add/$',
        view=LocationCreateView.as_view(),
        name='location_add'
    ),

    url(
        regex=r'^parasha/$',
        view=ParashaListView.as_view(),
        name='parasha'
    ),
    url(
        regex=r'^parasha/(?P<pk>[0-9]+)/$',
        view=ParashaDetailView.as_view(),
        name='parasha_detail'
    ),
    url(
        regex=r'^parasha/(?P<pk>[0-9]+)/edit/$',
        view=ParashaUpdateView.as_view(),
        name='parasha_edit'
    ),

    url(
        regex=r'^reading/$',
        view=ReadingListView.as_view(),
        name='reading'
    ),
    url(
        regex=r'^reading/(?P<pk>[0-9]+)/edit/$',
        view=ReadingUpdateView.as_view(),
        name='reading_edit'
    ),
    url(
        regex=r'^reading/add/$',
        view=ReadingCreateView.as_view(),
        name='reading_add'
    ),

    url(
        regex=r'^word/$',
        view=WordListView.as_view(),
        name='word'
    ),
    url(
        regex=r'^word/(?P<pk>[0-9]+)/$',
        view=WordDetailView.as_view(),
        name='word_detail'
    ),
    url(
        regex=r'^word/(?P<pk>[0-9]+)/edit/$',
        view=WordUpdateView.as_view(),
        name='word_edit'
    ),
    url(
        regex=r'^word/add/$',
        view=WordCreateView.as_view(),
        name='word_add'
    ),

    url(
        regex=r'^$',
        view=TemplateView.as_view(template_name='bytes/index.html'),
        name='index'),
]
