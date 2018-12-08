from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import Politoon


def index(request):
    return render(request, 'index.html')


def alltoons(request):
    all_toons = Politoon.objects.all()
    print(all_toons)
    # print(all_toons)
    # return render(request, 'toons.html')
    return render(request, 'toons.html', context={'all_toons': all_toons})


def thistoon(request, asd):
    print(asd)
    detail = Politoon.objects.get(name=asd)
    print(detail)
    return render(request, 'detail.html', context={'detail': detail})
    # return HttpResponse('Slug parameter is: ' + asd)
