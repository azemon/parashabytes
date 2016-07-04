from django.core.exceptions import ValidationError
from django.forms import CharField, HiddenInput, ModelForm

from bible.views import NormalizeLocation
from .models import Location, Parasha, Reading, Word


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['book', 'chapter', 'verse']


class ParashaForm(ModelForm):
    class Meta:
        model = Parasha
        fields = ['hebrew_name', 'transliterated_name', 'notes']


class ReadingForm(ModelForm):
    class Meta:
        model = Reading
        fields = ['book', 'start_chapter', 'start_verse', 'end_chapter', 'end_verse']


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['english_word', 'hebrew_word', 'transliterated_word', 'description', 'location']


class LocationField(CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.response = {}

    def clean(self, value):
        clean_value = super().clean(value)
        self.response = NormalizeLocation(reference=clean_value)
        try:
            clean_value = self.response['ref']
            return clean_value
        except KeyError:
            raise ValidationError(self.response['error'])


class NewWordForm(ModelForm):
    locations = LocationField(label='Location(s)')

    class Meta:
        model = Word
        fields = ['english_word', 'hebrew_word', 'transliterated_word', 'description', 'location']
        widgets = {
            'location': HiddenInput(),
        }

    def clean_locations(self):
        sefaria_response = self.fields['locations'].response
        book_name = sefaria_response['book']['english']
        chapter = sefaria_response['chapter']
        verse = sefaria_response['verse']
        return self.cleaned_data['locations']
