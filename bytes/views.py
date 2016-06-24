from django.shortcuts import get_object_or_404, render

from .models import Parasha


def parasha_list(request):
    """
    list all parashot
    :return:
    """
    parashot = Parasha.objects.all()
    return render(request, 'bytes/parasha_list.html', {'parashot': parashot})


def parasha_detail(request, pk):
    parasha = get_object_or_404(Parasha, pk=pk)
    return render(request, 'bytes/parasha_detail.html', {'parasha': parasha})
