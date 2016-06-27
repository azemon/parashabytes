from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from braces.views import LoginRequiredMixin

from .forms import ParashaForm, ReadingForm
from .models import Parasha, Reading


class ParashaDetailView(DetailView):
    model = Parasha
    template_name = 'bytes/parasha_detail.html'
    context_object_name = 'parasha'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parasha = context['parasha']
        word_list = []
        for word in parasha.word_set():
            word.parasha(parasha)
            word_list.append(word)
        context.update({
            'word_list': sorted(word_list)
        })
        return context


class ParashaUpdateView(LoginRequiredMixin, UpdateView):
    model = Parasha
    form_class = ParashaForm
    template_name = 'bytes/parasha_update.html'
    success_url = reverse_lazy('bytes:parasha')
    login_url = reverse_lazy('admin:login')


class ParashaListView(ListView):
    model = Parasha
    template_name = 'bytes/parasha_list.html'
    context_object_name = 'parashot'


class ReadingCreateView(LoginRequiredMixin, CreateView):
    model = Reading
    form_class = ReadingForm
    template_name = 'bytes/reading_create.html'
    success_url = reverse_lazy('bytes:reading')
    login_url = reverse_lazy('admin:login')


class ReadingListView(ListView):
    model = Reading
    template_name = 'bytes/reading_list.html'
    context_object_name = 'readings'


class ReadingUpdateView(LoginRequiredMixin, UpdateView):
    model = Reading
    form_class = ReadingForm
    template_name = 'bytes/reading_update.html'
    success_url = reverse_lazy('bytes:reading')
    login_url = reverse_lazy('admin:login')
