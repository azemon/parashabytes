from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ParashaForm, ReadingForm
from .models import Parasha, Reading


class ParashaDetailView(DetailView):
    model = Parasha
    template_name = 'bytes/parasha_detail.html'
    context_object_name = 'parasha'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parasha = context['parasha']
        # todo: created a set of locations for each word, restricted by the parasha's locations
        location_list = []
        for word in parasha.word_set():
            location_set = word.location.all()
            for location in location_set:
                location_list.append(location)
        context.update({
            'word_set': parasha.word_set()
        })
        return context


class ParashaUpdateView(UpdateView):
    model = Parasha
    form_class = ParashaForm
    template_name = 'bytes/parasha_update.html'
    success_url = reverse_lazy('bytes:parasha')


class ParashaListView(ListView):
    model = Parasha
    template_name = 'bytes/parasha_list.html'
    context_object_name = 'parashot'


class ReadingCreateView(CreateView):
    model = Reading
    form_class = ReadingForm
    template_name = 'bytes/reading_create.html'
    success_url = reverse_lazy('bytes:reading')


class ReadingListView(ListView):
    model = Reading
    template_name = 'bytes/reading_list.html'
    context_object_name = 'readings'


class ReadingUpdateView(UpdateView):
    model = Reading
    form_class = ReadingForm
    template_name = 'bytes/reading_update.html'
    success_url = reverse_lazy('bytes:reading')
