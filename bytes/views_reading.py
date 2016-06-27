from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from braces.views import LoginRequiredMixin

from .forms import ReadingForm
from .models import Reading


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
