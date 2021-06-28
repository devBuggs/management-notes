from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from django.template import loader

from accounts.models import UserSubscription
from .models import CourseSemester, SemesterSubject, SubjectUnit

# Create your views here
"""
@login_required
def dashboard_view(request):
    currentUser = request.user
    subscription = UserSubscription.objects.get(username=currentUser.id)
    subscriptionAccess = subscription.subscription
    courseAccess = subscription.course
    semList = CourseSemester.objects.filter(course_name = courseAccess).in_bulk()
    print("--------------------> Semester List: ", semList)
    context = {
        'layout': 1,
        'footer': 0,
        'navType': 'semester',
        'accessType': str(subscriptionAccess),
        'subject': str(courseAccess),
        'navlink': semList.values(),
    }
    return render(request, "course/main.html", context)

@login_required
def sub_view(request, semester_code):
    currentUser = request.user
    subscription = UserSubscription.objects.get(username=currentUser.id)
    subscriptionType = subscription.subscription
    courseAccess = subscription.course
    semInfo = CourseSemester.objects.get(code= semester_code)
    subjectList = SemesterSubject.objects.filter(semester_code = semInfo).in_bulk()
    print("--------------->", type(semester_code))
    context = {
        'layout': 1,
        'footer': 0,
        'navType': 'subject',
        'accessType': str(subscriptionType),
        'subject': str(courseAccess),
        'navlink': subjectList.values(),
        #'sesesterID': semester_code,
    }
    return render(request, "course/main.html", context)

@login_required
def unit_view(request, semester_code, subject_code):
    currentUser = request.user
    subscription = UserSubscription.objects.get(username=currentUser.id)
    subscriptionType = subscription.subscription
    courseAccess = subscription.course
    semInfo = CourseSemester.objects.get(code= semester_code)
    subInfo = SemesterSubject.objects.get(code= subject_code)
    unitList = SubjectUnit.objects.filter(subject_code = subInfo).in_bulk()
    context = {
        'layout': 1,
        'footer': 0,
        'navType': 'unit',
        'accessType': str(subscriptionType),
        'subject': str(courseAccess),
        'navlink': unitList.values(),
        'semester_code': semester_code,
    }
    return render(request, "course/main.html", context)

@login_required
def data_view(request, semester_code, subject_code, unit_code):
    semID = semester_code
    subCode = subject_code
    unitNo = unit_code
    currentUser = request.user
    subscription = UserSubscription.objects.get(username=currentUser.id)
    subscriptionType = subscription.subscription
    courseAccess = subscription.course
    semInfo = CourseSemester.objects.get(code= semester_code)
    subInfo = SemesterSubject.objects.get(code= subject_code)
    unitList = SubjectUnit.objects.filter(subject_code = subInfo).in_bulk()
    
    fileName = "course/source/"+str(semID)+str(subCode)+str(unitNo)+".html"
    template = loader.get_template(fileName)
    context = {
        'layout': 1,
        'footer': 0,
        'navType': 'unit',
        'accessType': str(subscriptionType),
        'subject': str(courseAccess),
        'navlink': unitList.values(),
        'semester_code': semester_code,
    }
    return HttpResponse(template.render(context, request))

@login_required
def sub_view(request, semester_code):
    currentUser = request.user
    subscription = UserSubscription.objects.get(username=currentUser.id)
    subscriptionType = subscription.subscription
    courseAccess = subscription.course
    semInfo = CourseSemester.objects.get(code= semester_code)
    subjectList = SemesterSubject.objects.filter(semester_code = semInfo).in_bulk()
    print("--------------->", semester_code)
    print("--------------->", type(semInfo))
    print(semInfo.code)
    context = {
        'layout': 1,
        'footer': 0,
        'navType': 'subject',
        'accessType': str(subscriptionType),
        'subject': str(courseAccess),
        'navlink': subjectList.values(),
        'semesterID': semInfo.code,         #extra data for url trailing
    }
    return render(request, "course/main.html", context)

"""

@login_required
def dashboard_view(request):
    userSubscription = UserSubscription.objects.get(username=request.user.id)
    subscriptionAccess = userSubscription.subscription
    courseAccess = userSubscription.course
    semList = CourseSemester.objects.filter(course_name = courseAccess).in_bulk()
    print("--------------------> Semester List: ", semList)
    context = {
        'layout': 1,
        'footer': 0,
        'navType': 'semester',
        'accessType': str(subscriptionAccess),
        'subject': str(courseAccess),
        'navlink': semList.values(),
    }
    return render(request, "course/main.html", context)

@login_required
def sub_view(request, semester_code):
    userSubscription = UserSubscription.objects.get(username=request.user.id)
    subscriptionType = userSubscription.subscription
    courseAccess = userSubscription.course
    sem_info = CourseSemester.objects.get(code= semester_code)
    subjectList = SemesterSubject.objects.filter(semester_code = sem_info).in_bulk()
    #print("--------------->", semester_code)
    #print("--------------->", type(sem_info))
    print(sem_info.code)
    context = {
        'layout': 1,
        'footer': 0,
        'navType': 'subject',
        'accessType': str(subscriptionType),
        'subject': str(courseAccess),
        'navlink': subjectList.values(),
        'semesterID': sem_info.code,         #extra data for url trailing
    }
    return render(request, "course/main.html", context)

@login_required
def unit_view(request, semesterID, subjectID):
    currentUser = request.user
    userSubscription = UserSubscription.objects.get(username=currentUser.id)
    subscriptionType = userSubscription.subscription
    courseAccess = userSubscription.course
    sem_info = CourseSemester.objects.get(code= semesterID)
    sub_info = SemesterSubject.objects.get(code= subjectID)
    unitList = SubjectUnit.objects.filter(subject_code = sub_info).in_bulk()
    context = {
        'layout': 1,
        'footer': 0,
        'navType': 'unit',
        'accessType': str(subscriptionType),
        'subject': str(courseAccess),
        'navlink': unitList.values(),
        'semesterID': sem_info.code,
        'subjectID': sub_info.code,
    }
    return render(request, "course/main.html", context)

@login_required
def data_view(request, semesterID, subjectID, unit_code):
    semID = semesterID
    subCode = subjectID
    unitNo = unit_code
    print("---------------------> ", semID)
    print("---------------------> ", subCode)
    print("---------------------> ", unitNo)
    currentUser = request.user
    subscription = UserSubscription.objects.get(username=currentUser.id)
    subscriptionType = subscription.subscription
    courseAccess = subscription.course
    sem_info = CourseSemester.objects.get(code= semID)
    sub_info = SemesterSubject.objects.get(code= subCode)
    unitList = SubjectUnit.objects.filter(subject_code = sub_info).in_bulk()
    
    fileName = "course/source/"+str(semID)+str(subCode)+str(unitNo)+".html"
    template = loader.get_template(fileName)
    context = {
        'layout': 1,
        'footer': 0,
        'navType': 'unit',
        'accessType': str(subscriptionType),
        'subject': str(courseAccess),
        'navlink': unitList.values(),
        'semesterID': sem_info.code,
        'subjectID': sub_info.code,
    }
    return HttpResponse(template.render(context, request))

