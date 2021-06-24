from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# import models here
from .models import contact, ClientReview
from courseapp.models import CourseSemester, SemesterSubject, SubjectUnit
from accounts.models import Course

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
    if request.method == 'POST':
        search_keyword = request.POST['homeSearch']
        print("-------------------> ", search_keyword)
        #
        # Logic for searching in database's multiple table or an indexed table to fetch the related query
        #
        if search_keyword is not None:
            print("-------------------> Searching in database outside index_view ..............")
            #
            # Logic for query and getting the exact match 
            #
            courseList = Course.objects.all()
            #print(courseList)
            semSubjectList = SemesterSubject.objects.all()
            #print(semSubjectList)
            subUnitList = SubjectUnit.objects.all()
            #print(subUnitList)
        return HttpResponse("Search is under construction. #ecorpians")
    return HttpResponse("No data to search...")