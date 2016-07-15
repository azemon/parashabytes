from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.db import IntegrityError
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView

from braces.views import LoginRequiredMixin

from .forms import LocationForm
from .models import Location
from .views_util import ConfirmationMessageMixin


class LocationCreateView(LoginRequiredMixin, ConfirmationMessageMixin, CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'bytes/location_create.html'
    success_url = reverse_lazy('bytes:location')
    success_message = 'Location successfully added'

    def form_valid(self, form):
        try:
            response = super(CreateView, self).form_valid(form)
        except IntegrityError:
            messages.error(self.request, 'Location already exists. Not added.')
            return redirect(self.success_url)
        else:
            messages.info(self.request, self.success_message)
            return response


class LocationListView(ListView):
    model = Location
    template_name = 'bytes/location_list.html'
    context_object_name = 'locations'
