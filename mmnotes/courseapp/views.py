from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from django.template import loader

from accounts.models import UserSubscription
from .models import CourseSemester, SemesterSubject, SubjectUnit

# Create your views here.

@login_required
def subject_view(request):
    currentUser = request.user
    subscription = UserSubscription.objects.get(username=currentUser.id)
    accessType = subscription.subscription_details
    subjectAccess = subscription.subject_details
    semList = CourseSemester.objects.filter(course_name = subjectAccess).in_bulk()
    print("===================== sem List", semList, "--------------- type :", type(semList))
    print("-------------- ", semList.values())
    context = {
        'layout': 1,
        'footer': 0,
        'navType': 'semester',
        'accessType': str(accessType),
        'subject': str(subjectAccess),
        'navlink': semList.values(),
    }
    return render(request, "course/main.html", context)

@login_required
def sub_view(request, semester_code):
    currentUser = request.user
    subscription = UserSubscription.objects.get(username=currentUser.id)
    accessType = subscription.subscription_details
    subjectAccess = subscription.subject_details
    semInfo = CourseSemester.objects.get(semester_code= semester_code)
    subjectList = SemesterSubject.objects.filter(semester_code = semInfo).in_bulk()
    print("===================== subject List", subjectList, "--------------- type :", type(subjectList))
    print("-------------- ", subjectList.values())
    context = {
        'layout': 1,
        'footer': 0,
        'navType': 'subject',
        'accessType': str(accessType),
        'subject': str(subjectAccess),
        'navlink': subjectList.values(),
    }
    return render(request, "course/main.html", context)

@login_required
def unit_view(request, semester_code, subject_code):
    currentUser = request.user
    subscription = UserSubscription.objects.get(username=currentUser.id)
    accessType = subscription.subscription_details
    subjectAccess = subscription.subject_details
    semInfo = CourseSemester.objects.get(semester_code= semester_code)
    subInfo = SemesterSubject.objects.get(subject_code= subject_code)
    unitList = SubjectUnit.objects.filter(subject_code = subInfo).in_bulk()
    print("===================== unit List", unitList, "--------------- type :", type(unitList))
    print("-------------- ", unitList.values())
    context = {
        'layout': 1,
        'footer': 0,
        'navType': 'unit',
        'accessType': str(accessType),
        'subject': str(subjectAccess),
        'navlink': unitList.values(),
    }
    return render(request, "course/main.html", context)

@login_required
def data_view(request, semester_code, subject_code, unit_code):
    semID = semester_code
    subCode = subject_code
    unitNo = unit_code
    
    currentUser = request.user
    subscription = UserSubscription.objects.get(username=currentUser.id)
    accessType = subscription.subscription_details
    subjectAccess = subscription.subject_details
    semInfo = CourseSemester.objects.get(semester_code= semester_code)
    subInfo = SemesterSubject.objects.get(subject_code= subject_code)
    unitList = SubjectUnit.objects.filter(subject_code = subInfo).in_bulk()
    print("===================== unit List", unitList, "--------------- type :", type(unitList))
    print("-------------- ", unitList.values())
    
    fileName = "course/source/"+str(semID)+str(subCode)+str(unitNo)+".html"
    print("*******************************************", fileName)
    template = loader.get_template(fileName)
    context = {
        'layout': 1,
        'footer': 0,
        'navType': 'unit',
        'accessType': str(accessType),
        'subject': str(subjectAccess),
        'navlink': unitList.values(),
    }
    return HttpResponse(template.render(context, request))

@login_required
def testUI(request):
    currentUser = request.user
    subscription = UserSubscription.objects.get(username=currentUser.id)
    accessType = subscription.subscription_details
    subjectAccess = subscription.subject_details
    semInfo = CourseSemester.objects.get(semester_code= semester_code)
    subInfo = SemesterSubject.objects.get(subject_code= subject_code)
    unitList = SubjectUnit.objects.filter(subject_code = subInfo).in_bulk()
    print("===================== unit List", unitList, "--------------- type :", type(unitList))
    print("-------------- ", unitList.values())
    context = {
        'layout': 1,
        'footer': 0,
        'navType': 'unit',
        'accessType': str(accessType),
        'subject': str(subjectAccess),
        'navlink': unitList.values(),
    }
    return render(request, 'course/BCintro.html', context)