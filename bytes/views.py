from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .forms import ParashaForm, PortionForm
from .models import Parasha, Portion


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
def portion_edit(request, pk=None):
    success = None
    if pk is not None:
        portion = get_object_or_404(Portion, pk=pk)
        button = 'Update'
    else:
        portion = Portion()
        button = 'Add'
    if 'POST' == request.method:
        form = PortionForm(request.POST, instance=portion)
        if form.is_valid():
            form.save()
            success = 'Portion updated'
    else:
        form = PortionForm(None, instance=portion)
    return render(request, 'bytes/portion_edit.html',
                  {'portion': portion, 'form': form, 'success': success, 'button': button})


def portion_list(request):
    """
    list all portions of the Tenach
    :return:
    """
    portions = Portion.objects.all()
    return render(request, 'bytes/portion_list.html', {'portions': portions})
