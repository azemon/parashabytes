from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse


class ConfirmationMessageMixin(object):
    """
    add to any class based view to make it easy to display a confirmation, e.g. use on create/update/delete views
    Usage:
        in the CBV:         class WhateverView(ConfirmationMessageMixin, ...):
                                success_message = 'whatever successfully updated'

        see https://docs.djangoproject.com/en/1.9/ref/contrib/messages/#displaying-messages for how to
        display the messages
    """

    @property
    def success_message(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_message)
        return super(ConfirmationMessageMixin, self).form_valid(form)


def login_view(request):
    template = 'bytes/login.html'

    if 'GET' == request.method:
        try:
            next_page = request.GET['next']
        except KeyError:
            next_page = reverse('bytes:index')
        return render(request, template, {'next': next_page})
    else:
        logout(request)
        try:
            next_page = request.POST['next']
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            return render(request, template)

        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.info(request, 'Welcome {first} {last}'.format(first=user.first_name, last=user.last_name))
            return HttpResponseRedirect(next_page)
        else:
            messages.error(request, 'Login incorrect')
            return render(request, template, {'next': next_page, 'username': username})
