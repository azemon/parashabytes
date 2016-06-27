from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from braces.views import LoginRequiredMixin

from .forms import ParashaForm
from .models import Parasha


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


class ParashaListView(ListView):
    model = Parasha
    template_name = 'bytes/parasha_list.html'
    context_object_name = 'parashot'


class ParashaUpdateView(LoginRequiredMixin, UpdateView):
    model = Parasha
    form_class = ParashaForm
    template_name = 'bytes/parasha_update.html'
    success_url = reverse_lazy('bytes:parasha')
    login_url = reverse_lazy('admin:login')
