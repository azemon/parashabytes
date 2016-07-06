import json

from django.core.management.base import BaseCommand

from bible.models import Bible

# see http://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database

FILES = (
    'Genesis-hebrew.json',
)


class Command(BaseCommand):
    args = ''
    help = 'Load Hebrew text of the Torah'

    def handle(self, *args, **options):
        Bible.objects.all().delete()

        for filename in FILES:
            data = json.load(open('bible/data/' + filename))

            for chapter in range(0, len(data['text'])):
                verses = data['text'][chapter]
                for verse in range(0, len(verses)):
                    c = chapter + 1
                    v = verse + 1
                    t = verses[verse]
                    b = Bible.objects.create(
                        book=data['title'],
                        chapter=c,
                        verse=v,
                        hebrew_text=t
                    )
                    pass
            return
