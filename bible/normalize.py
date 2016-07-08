import requests


def NormalizeLocation(reference):
    """
    Normalize a location, turning "gen 1:1" into "Genesis 1:1"
    also returns the book title in English and Hebrew as well as broken out chapter and verse numbers
    :param reference: Bible reference of the form "Genesis 1:1"
    :return: dict
    """
    error_response = {
        'error': 'invalid location',
    }

    sefaria_url = 'http://www.sefaria.org/api/texts/{reference}?context=0&commentary=0'.format(
        reference=reference.replace(' ', '.')
    )
    data = requests.get(sefaria_url).json()

    try:
        if '' != data['text']:
            response = {
                'ref': data['ref'],
                'book': {
                    'english': data['book'],
                    'hebrew': data['heTitle'],
                },
                'chapter': data['sections'][0],
                'verse': data['sections'][1],
            }
        else:
            # invalid verse lands here
            response = error_response
    except KeyError:
        # invalid book name or chapter lands here
        response = error_response
    return response
