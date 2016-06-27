from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from braces.views import LoginRequiredMixin

from .forms import WordForm
from .models import Word


class WordCreateView(LoginRequiredMixin, CreateView):
    model = Word
    form_class = WordForm
    template_name = 'bytes/word_create.html'
    success_url = reverse_lazy('bytes:word')
    login_url = reverse_lazy('admin:login')


class WordDetailView(DetailView):
    model = Word
    template_name = 'bytes/word_detail.html'
    context_object_name = 'word'


class WordListView(ListView):
    model = Word
    template_name = 'bytes/word_list.html'
    context_object_name = 'words'


class WordUpdateView(LoginRequiredMixin, UpdateView):
    model = Word
    form_class = WordForm
    template_name = 'bytes/word_update.html'
    success_url = reverse_lazy('bytes:word')
    login_url = reverse_lazy('admin:login')
