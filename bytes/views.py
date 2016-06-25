from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .forms import ParashaForm, ReadingForm
from .models import Parasha, Reading


def parasha_detail(request, pk):
    parasha = get_object_or_404(Parasha, pk=pk)
    return render(request, 'bytes/parasha_detail.html', {'parasha': parasha})


@login_required
def parasha_edit(request, pk):
    success = None
    parasha = get_object_or_404(Parasha, pk=pk)
    if 'POST' == request.method:
        form = ParashaForm(request.POST, instance=parasha)
        if form.is_valid():
            form.save()
            success = 'Parasha updated'
    else:
        form = ParashaForm(None, instance=parasha)
    return render(request, 'bytes/parasha_edit.html', {'parasha': parasha, 'form': form, 'success': success})


def parasha_list(request):
    """
    list all parashot
    :return:
    """
    parashot = Parasha.objects.all()
    return render(request, 'bytes/parasha_list.html', {'parashot': parashot})


@login_required
def reading_edit(request, pk=None):
    success = None
    if pk is not None:
        reading = get_object_or_404(Reading, pk=pk)
        button = 'Update'
    else:
        reading = Reading()
        button = 'Add'
    if 'POST' == request.method:
        form = ReadingForm(request.POST, instance=reading)
        if form.is_valid():
            form.save()
            success = 'Reading updated'
    else:
        form = ReadingForm(None, instance=reading)
    return render(request, 'bytes/reading_edit.html',
                  {'reading': reading, 'form': form, 'success': success, 'button': button})


def reading_list(request):
    """
    list all readings of the Tenach
    :return:
    """
    readings = Reading.objects.all()
    return render(request, 'bytes/reading_list.html', {'readings': readings})
