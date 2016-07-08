import json

import requests
from django.http import HttpResponse

from .normalize import NormalizeLocation


def TextRetrieveView(request, reference):
    """
    retrieve some text from Sefaria and return it
    :param request: httprequest
    :param reference: Bible reference of the form "Genesis 1:1"
    :return:
    """
    sefaria_url = 'http://www.sefaria.org/api/texts/{reference}?context=0&commentary=0'.format(
        reference=reference.replace(' ', '.')
    )
    data = requests.get(sefaria_url).json()
    text = {
        'english': data['text'],
        'hebrew': data['he'],
    }
    return HttpResponse(json.dumps(text), content_type='application/json')


def NormalizeLocationView(request, reference):
    """
    Normalize a location, turning "gen 1:1" into "Genesis 1:1"
    also returns the book title in English and Hebrew as well as broken out chapter and verse numbers
    :param request: httprequest
    :param reference: Bible reference of the form "Genesis 1:1"
    :return: HttpResponse
    """
    response = NormalizeLocation(reference)
    return HttpResponse(json.dumps(response), content_type='application/json')
