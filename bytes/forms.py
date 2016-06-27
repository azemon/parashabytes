from django.forms import ModelForm

from .models import Location, Parasha, Reading, Word


class LocationForm(ModelForm):
    class Meta:
        model = Location
        exclude = ['sortkey']


class ParashaForm(ModelForm):
    class Meta:
        model = Parasha
        exclude = []


class ReadingForm(ModelForm):
    class Meta:
        model = Reading
        exclude = ['start_sortkey', 'end_sortkey', 'description']

class WordForm(ModelForm):
    class Meta:
        model = Word
        exclude = []
