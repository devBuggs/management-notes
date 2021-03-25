from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.utils import timezone


# Create your views here.
def index(request):
    return render(request, 'web/index.html', context=None)
