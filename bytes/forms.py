from django.forms import ModelForm

from .models import Parasha, Portion


class ParashaForm(ModelForm):
    class Meta:
        model = Parasha
        exclude = []


class PortionForm(ModelForm):
    class Meta:
        model = Portion
        exclude = ['start_sortkey', 'end_sortkey', 'description']
