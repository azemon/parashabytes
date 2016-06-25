from django.forms import ModelForm

from .models import Parasha, Reading


class ParashaForm(ModelForm):
    class Meta:
        model = Parasha
        exclude = []


class ReadingForm(ModelForm):
    class Meta:
        model = Reading
        exclude = ['start_sortkey', 'end_sortkey', 'description']
