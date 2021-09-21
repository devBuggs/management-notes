from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from itertools import chain

from django.views.generic import ListView

# import models here
from .models import contact, ClientReview

# import models for searching
from courseapp.models import CourseSemester, SemesterSubject, SubjectUnit
from accounts.models import Course

# import forms here
from .forms import contact_form

# Create your views here.
def index(request):
    if request.method == 'POST':
        #searchValue = request.POST
        #print("-------------------> Search value:", searchValue)
        return HttpResponse("index post method. ECORPIN CORP")
    else:
        review_list = ClientReview.objects.all()
        print("------------------->", review_list)
        context = {
            'review_list' : review_list,
        }
    return render(request, 'web/index.html', context)

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

def about_view(request):
    context = {
        
    }
    return render(request, 'web/about.html', context)

class SearchView(ListView):
    template_name = 'web/search_result.html'
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('homeSearch')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('homeSearch')
        # validate query
        if query is not None:
            print("-------------------> Searching in database outside index_view ..............")
            course_results = Course.objects.search(query)
            semester_results = CourseSemester.objects.search(query)
            subject_results = SemesterSubject.objects.search(query)
            unit_results = SubjectUnit.objects.search(query)

            # combine querysets
            queryset_chain = chain(
                course_results,
                semester_results,
                subject_results,
                unit_results
            )
            qs = sorted(queryset_chain, key=lambda instance: instance.pk, reverse=True)
            self.count = len(qs) # since qs is actually a list
            return qs
        return Course.objects.none() # just qs is actually a list

def privacy_view(request):
    form = contact_form()
    context = { 'form':form }
    return render(request, 'web/privacy.html', context)

def tou_view(request):
    form = contact_form()
    context = { 'form':form }
    return render(request, 'web/tou.html', context)
