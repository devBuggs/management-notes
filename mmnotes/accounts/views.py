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
        userSub = UserSubscription(username=user, subscription_details=default_pack, subject_details=default_access)
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
        user = User.objects.get(id=request.user.id)
        fname = form.cleaned_data.get('first_name')
        lname = form.cleaned_data.get('last_name')
        user.first_name = str(fname)
        user.last_name = str(lname)
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
    if request.method == "POST":
        if form.is_valid():
            username = str(request.user.username)
            contactNo = form.cleaned_data.get('contact_number')
            contact = UserContact.objects.filter(username=username)
            if contact:
                currentContact = UserContact.objects.get(username=username)
                currentContact.contact_number = contactNo
                currentContact.save()
                return redirect(profile_view)
            else:
                contact = UserContact.objects.create(username=username, contact_number=contactNo)
                contact.save()
                return redirect(profile_view)
        context = {
            'form': form,
            'type': 'contact',
            'footer': 0,
        }
        return render(request, 'accounts/editcontact.html', context)
    else:
        username = request.user.username
        contact = UserContact.objects.filter(username=username)
        if contact:
            currentContact = UserContact.objects.get(username=username)
            context = {
                'form': form,
                'type': 'contact',
                'footer': 0,
                'contact': currentContact.contact_number,
            }
            return render(request, 'accounts/editcontact.html', context)
        else:
            print("No Contact exist")
            context = {
                'form': form,
                'type': 'contact',
                'footer': 0,
            }
            return render(request, 'accounts/editcontact.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile_view(request):
    currentUser = request.user
    isNameNone = False
    isContactNone = False
    subscription = UserSubscription.objects.get(username=currentUser.id)
    contact = UserContact.objects.filter(username=str(currentUser.username))
    print("---------------", contact)
    accessType = subscription.subscription_details
    subjectAccess = subscription.subject_details
    # TODO check user_fname, user_lname and user_contact
    if currentUser.first_name == "" and currentUser.last_name == "":
        #print("----------------------- Incomplete profile -----------------------")
        isNameNone = True 
    if contact.exists():
        print("----------------------- contact found -----------------------")
        print("---------------", contact)
    else:
        print("----------------------- No contact found -----------------------")
        isContactNone = True
    context = {
        'layout': 0,
        'footer': 0,
        'accessType': str(accessType),
        'subject': str(subjectAccess),
        'nameAlert': isNameNone,
        'contactAlert': isContactNone,
    }
    return render(request, "accounts/profile.html", context)
