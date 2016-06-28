from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.db import IntegrityError
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView

from braces.views import LoginRequiredMixin

from .forms import ReadingForm
from .models import Reading
from .views_util import ConfirmationMessageMixin


class ReadingCreateView(LoginRequiredMixin, ConfirmationMessageMixin, CreateView):
    model = Reading
    form_class = ReadingForm
    template_name = 'bytes/reading_create.html'
    success_url = reverse_lazy('bytes:reading')
    success_message = 'Reading successfully added'
    login_url = reverse_lazy('admin:login')

    def form_valid(self, form):
        try:
            response = super(CreateView, self).form_valid(form)
        except IntegrityError:
            messages.error(self.request, 'Reading already exists. Not added.')
            return redirect(self.success_url)
        else:
            messages.info(self.request, self.success_message)
            return response


class ReadingListView(ListView):
    model = Reading
    template_name = 'bytes/reading_list.html'
    context_object_name = 'readings'


class ReadingUpdateView(LoginRequiredMixin, ConfirmationMessageMixin, UpdateView):
    model = Reading
    form_class = ReadingForm
    template_name = 'bytes/reading_update.html'
    success_url = reverse_lazy('bytes:reading')
    success_message = 'Reading successfully updated'
    login_url = reverse_lazy('admin:login')
