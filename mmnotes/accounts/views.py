import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login, logout


# import models here
from django.contrib.auth.models import User

from accounts.models import UserSubscription, SubscriptionPack, Course, UserContact

# import forms here
from .forms import UserLoginForm, UserRegisterForm, EditUserProfileForm, EditContactForm


# Global Instance
default_pack = SubscriptionPack.objects.get(id=1)
default_access = Course.objects.get(id=2)


# Create your views here.

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
        # Redirect to HOME-VIEW
        return redirect(profile_view)
    context = {
        'form': form,
        'layout': 1,
        'footer': 0,
    }
    return render(request, 'accounts/login.html', context)

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        # Subscription details of correspondance user
        userSub = UserSubscription(
            username=user, subscription_details=default_pack, subject_details=default_access)
        user.save()
        userSub.save()
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

@login_required
def editprofile_view(request):
    form = EditUserProfileForm(request.POST or None)
    if form.is_valid():
        #form = form.save()
        user = User.objects.get(id=request.user.id)
        print("Printing User : ", user)
        fname = form.cleaned_data.get('first_name')
        lname = form.cleaned_data.get('last_name')
        print("*************** fname : ", fname)
        print("*************** lname : ", lname)
        user.first_name = str(fname)
        user.last_name = str(lname)
        print("--------------- user.first_name : ", user.first_name)
        print("--------------- user.last_name : ", user.last_name)
        print("*************** assing fname = ", str(fname))
        print("*************** assing lname = ", str(lname))
        user.save()

        return redirect(profile_view)
    context = {
        'form': form,
        'footer': 0,
        }
    return render(request, 'accounts/editprofile.html', context)

@login_required
def editContact_view(request):
    form = EditContactForm(request.POST or None)
    if form.is_valid():
        username = str(request.user.username)
        contactNo = form.cleaned_data.get('contact_number')
        print("*********************** contact Number : ", contactNo)
        contact = UserContact.objects.create(username=username, contact_number=contactNo)
        contact.save()

        return redirect(profile_view)
    context = {
        'form': form,
        'type': 'contact',
        'footer': 0,
    }
    return render(request, 'accounts/editcontact.html', context)

def logout_view(request):
    logout(request)
    # Redirect to User-Login-Page
    return redirect('/')

@login_required
def profile_view(request):
    currentUser = request.user
    subscription = UserSubscription.objects.get(username=currentUser.id)
    accessType = subscription.subscription_details
    subjectAccess = subscription.subject_details
    context = {
        'layout': 0,
        'footer': 1,
        'accessType': str(accessType),
        'subject': str(subjectAccess),
    }
    return render(request, "accounts/profile.html", context)

@login_required
def payment_view(request):
    userName = str(request.user.username)
    userContactInfo = UserContact.objects.get(username=userName).contact_number 
    orderId = str(request.user.first_name[0:3])+str(request.user.last_name[0:3])+str(userContactInfo[4:9])
    orderAmount = '200'
    orderCurrency = 'INR'
    orderNote = 'Payment'
    customerName = request.user.first_name + request.user.last_name
    customerPhone = str(userContactInfo)
    customerEmail = request.user.email

    postData = {
        "orderId" : orderId,
        "orderAmount" : orderAmount,
        "orderCurrency" : orderCurrency,
        "orderNote" : orderNote,
        "customerName" : customerName,
        "customerPhone" : customerPhone,
        "customerEmail" : customerEmail,
    }
    
    context = {
        'layout': 0,
        'footer': 0,
        'payment': postData
    }
    return render(request, 'accounts/checkout.html', context)


