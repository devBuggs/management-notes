import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User

# import models here
from .models import UserSubscription, SubscriptionPack, Course, UserContact

# import forms here
from .forms import UserLoginForm, UserRegisterForm

# global instance variable
default_pack = SubscriptionPack.objects.get(id=1)
default_access = Course.objects.get(id=3)
default_mob = ''

# create your views here
def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        userSub = UserSubscription(username=user, subscription_details=default_pack, subject_details=default_access)
        userContact = UserContact.objects.create(username=user, contact_number=default_mob)
        user.save()
        userSub.save()
        userContact.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect(profile_view)
    context = {
        'form': form,
        'layout': 1,
        'footer': 0,
    }
    return render(request, "accounts/signup.html", context)

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect(profile_view)
    context = {
        'form': form,
        'layout': 1,
        'footer': 0,
    }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile_view(request):
    currentUser = request.user
    isAlert = False
    subscription = UserSubscription.objects.get(username=currentUser.id)
    contact = UserContact.objects.filter(username=currentUser.id)
    accessType = subscription.subscription
    subjectAccess = subscription.course
    if currentUser.first_name == "" and currentUser.last_name == "":
        isAlert = True 
    if contact.exists() and contact:
        currentContact = UserContact.objects.get(username= currentUser.id)
        if currentContact.contact_number == '':
            isAlert = True
    else:
        isAlert = True
    context = {
        'layout': 0,
        'footer': 0,
        'accessType': str(accessType),
        'subject': str(subjectAccess),
        'user_contact': currentContact.contact_number,
        'alert': isAlert,
    }
    return render(request, "accounts/profile.html", context)

@login_required
def editAccount_view(request):
    if request.method == 'POST':
        errorMsg = ''
        form_data = request.POST
        if form_data['fname'] != '' or form_data['lname'] != '' and form_data['contactNum'] != '' :
            user = User.objects.get(id=request.user.id)
            fname = form_data['fname']
            lname = form_data['lname']
            user.first_name = str(fname)
            user.last_name = str(lname)
            user.save()
            mob = form_data['contactNum']
            contact = UserContact.objects.filter(username=request.user.id)
            if contact:
                currentContact = UserContact.objects.get(username=request.user.id)
                currentContact.contact_number = mob
                currentContact.save()
                return redirect(profile_view)
            else:
                contact = UserContact.objects.create(username=request.user.id, contact_number=mob)
                contact.save()
                return redirect(profile_view)
        else:
            #print("------------------------ Error Occured! please try again! ------------------------")
            errorMsg = "Something went wrong! please try again!"
            context = {
            'footer': 0,
            'layout':0,
            'error': errorMsg
            }
            return render(request, 'accounts/editAccount.html', context)
    else:
        currentUser = request.user
        currentContact = ''
        nameUpdate = False
        contactUpdate = False
        contact = UserContact.objects.filter(username=currentUser.id)
        if contact.exists():
            currentContact = UserContact.objects.get(username=currentUser.id)
        else:
            contactUpdate = True
        if currentUser.first_name == "" and currentUser.last_name == "":
            nameUpdate = True
        context = {
            'footer': 0,
            'layout':0,
            'nameUpdate' : nameUpdate,
            'contactUpdate' : contactUpdate,
            'contact': currentContact.contact_number,
            }
        return render(request, 'accounts/editAccount.html', context)

'''
def register_view(request):
    return HttpResponse("YourCourse_accounts/register")
def login_view(request):
    return HttpResponse("YourCourse_accounts/login")
def logout_view(request):
    return HttpResponse("YourCourse_accounts/logout")
def profile_view(request):
    print(default_access.name)
    print(default_pack.subscription)
    return HttpResponse("YourCourse_accounts/profile")
def editAccount_view(request):
    return HttpResponse("YourCourse_accounts/edit_account")
'''