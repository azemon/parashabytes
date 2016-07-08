from django.core.exceptions import ValidationError
from django.forms import CharField, ModelForm

from bible.normalize import NormalizeLocation
from .models import Book, Location, Parasha, Reading, Word


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


class LocationField(CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.response = {}

    def clean(self, value):
        clean_value = super().clean(value)
        if '' == clean_value:
            return clean_value
        self.response = NormalizeLocation(reference=clean_value)
        try:
            clean_value = self.response['ref']
            return clean_value
        except KeyError:
            raise ValidationError(self.response['error'])


class WordForm(ModelForm):
    location_field = LocationField(label='New Location', required=False)

    class Meta:
        model = Word
        fields = ['english_word', 'hebrew_word', 'transliterated_word', 'description']

    def save(self, commit=True):
        word = super().save(commit)

        # get the normalized info about the location
        sefaria_response = self.fields['location_field'].response
        if 'book' in sefaria_response.keys():
            book_name = sefaria_response['book']['english']
            chapter = sefaria_response['chapter']
            verse = sefaria_response['verse']

            # associate the word with the location
            book = Book.objects.get(english_name=book_name)
            location = Location.objects.get_or_create(book=book, chapter=chapter, verse=verse)
            word.location.add(location[0])
            word.save()

        return word
