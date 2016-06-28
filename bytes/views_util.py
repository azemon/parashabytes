from django.contrib import messages


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
