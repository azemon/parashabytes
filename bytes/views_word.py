from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from braces.views import LoginRequiredMixin

from .forms import WordForm
from .models import Word
from .views_util import ConfirmationMessageMixin


class WordCreateView(LoginRequiredMixin, ConfirmationMessageMixin, CreateView):
    model = Word
    form_class = WordForm
    template_name = 'bytes/word_create.html'
    success_url = reverse_lazy('bytes:word')
    success_message = 'Word successfully added'
    login_url = reverse_lazy('admin:login')

    def form_valid(self, form):
        try:
            response = super(CreateView, self).form_valid(form)
        except IntegrityError:
            messages.error(self.request, 'Word already exists. Not added.')
            return redirect(self.success_url)
        else:
            messages.info(self.request, self.success_message)
            return response


class WordDetailView(DetailView):
    model = Word
    template_name = 'bytes/word_detail.html'
    context_object_name = 'word'


class WordListView(ListView):
    model = Word
    template_name = 'bytes/word_list.html'
    context_object_name = 'words'

    def get_queryset(self):
        # start with the default/full queryset
        queryset = super(WordListView, self).get_queryset()

        # get the q parameter from the URL
        q = self.request.GET.get('q')
        if q:
            # return a filtered queryset
            return queryset.filter(
                Q(english_word__icontains=q) |
                Q(hebrew_word__icontains=q) |
                Q(transliterated_word__icontains=q) |
                Q(description__icontains=q)
            )
        else:
            return queryset


class WordUpdateView(LoginRequiredMixin, ConfirmationMessageMixin, UpdateView):
    model = Word
    form_class = WordForm
    template_name = 'bytes/word_update.html'
    success_url = reverse_lazy('bytes:word')
    success_message = 'Word successfully updated'
    login_url = reverse_lazy('admin:login')
