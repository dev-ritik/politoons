from django.http import HttpResponse, Http404
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Politoon
from .serializers import ToonsSerializer

# Create your views here.
from myapp.models import Politoon


def index(request):
    return render(request, 'index.html')


def alltoons(request):
    all_toons = Politoon.objects.all()
    print(all_toons)
    return render(request, 'toons.html', context={'all_toons': all_toons})


def thistoon(request, toon):
    try:
        detail = Politoon.objects.get(name=toon)
    except Politoon.DoesNotExist:
        return render(request, '404error.html')
    print(detail)
    return render(request, 'detail.html', context={'detail': detail})
    # return HttpResponse('Slug parameter is: ' + asd)


class ListToonsView(generics.ListAPIView):
    """
    Get all toons.
    """
    queryset = Politoon.objects.all()
    serializer_class = ToonsSerializer


class ThisToonsView(generics.RetrieveAPIView):
    """
    To get a particular toon.
    """
    serializer_class = ToonsSerializer

    def get_object(self):
        feedback_id = self.kwargs['toon']
        print(feedback_id)
        return get_object_or_404(Politoon, name=feedback_id)
