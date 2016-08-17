from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from braces.views import LoginRequiredMixin

from .forms import WordForm
from .models import Word, Location
from .views_util import ConfirmationMessageMixin


class WordCreateView(LoginRequiredMixin, ConfirmationMessageMixin, CreateView):
    model = Word
    form_class = WordForm
    template_name = 'bytes/word_create.html'
    success_url = reverse_lazy('bytes:word')
    success_message = 'Word successfully added'

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

    def get_queryset(self):
        queryset = super(WordDetailView, self).get_queryset()
        return queryset.prefetch_related('location')


class WordListView(ListView):
    model = Word
    template_name = 'bytes/word_list.html'
    context_object_name = 'words'

    def get_queryset(self):
        # start with the default/full queryset
        queryset = super(WordListView, self).get_queryset()
        queryset = queryset.prefetch_related('location')

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
    success_message = 'Word successfully updated'

    def get_queryset(self):
        queryset = super(WordUpdateView, self).get_queryset()
        return queryset.prefetch_related('location')

    def get_success_url(self):
        return reverse('bytes:word_detail', kwargs=self.kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'deletelocation' in request.POST:
            word = self.object
            location = Location.objects.get(pk=request.POST['deletelocation'])
            word.location.remove(location)
            messages.info(self.request, self.success_message)
            return HttpResponseRedirect(reverse_lazy('bytes:word_detail', kwargs={'slug': word.slug}))
        return super(UpdateView, self).post(request, *args, **kwargs)
