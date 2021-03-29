from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

# import models here
from .models import contact

from .forms import contact_form

# Create your views here.
def index(request):
    return render(request, 'web/index.html', context=None)


def contact_view(request):
    serverMsg = ''
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            serverMsg = "Your response is received. We'll get back to you shortly."
            return render(request, 'web/contact.html', { 'serverMsg':serverMsg })
    else:
        form = contact_form()
    context = { 'form':form }
    return render(request, 'web/contact.html', context)
