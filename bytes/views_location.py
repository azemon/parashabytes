from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from braces.views import LoginRequiredMixin

from .forms import LocationForm
from .models import Location


class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'bytes/location_create.html'
    success_url = reverse_lazy('bytes:location')
    login_url = reverse_lazy('admin:login')


class LocationListView(ListView):
    model = Location
    template_name = 'bytes/location_list.html'
    context_object_name = 'locations'
