from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from itertools import chain

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

def search_view(request):
    qs = []
    if request.method == 'POST':
        query = request.POST['homeSearch']
        if query is not None:
            print("-------------------> Searching in database outside index_view ..............")
            course_results = Course.objects.search(query)
            #semester_results = CourseSemester.objects.search(query, "semester_name")
            subject_results = SemesterSubject.objects.search(query, "subject_name")
            unit_results = SubjectUnit.objects.search(query, "unit_name")

            # combine querysets
            queryset_chain = chain(
                course_results,
                #semester_results,
                subject_results,
                unit_results
            )
            qs = sorted(queryset_chain, key=lambda instance: instance.pk, reverse=False)
            total_result = len(qs)
            print("----------------------------------------------------------------------------")
            #print("Type : ", qs[0].course_name, "\nQuery Set : ", qs)
            print("----------------------------------------------------------------------------")
        context = {
            "search_view" : True,
            'qs' : qs,
            'total_result' : total_result,
        }
        return render(request, 'web/contact.html', context)
    context = {
        "search_view" : True,
        'qs' : qs,
    }
    return render(request, 'web/contact.html', context)