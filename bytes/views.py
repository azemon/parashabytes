from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ParashaForm, ReadingForm
from .models import Parasha, Reading


class ParashaDetailView(DetailView):
    model = Parasha
    template_name = 'bytes/parasha_detail.html'
    context_object_name = 'parasha'


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
