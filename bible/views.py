import requests

import json;
from django.http import HttpResponse


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
    return HttpResponse(json.dumps(data), content_type='application/json')
