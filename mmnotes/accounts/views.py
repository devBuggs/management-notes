from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login, logout

# import models here
from django.contrib.auth.models import User
from accounts.models import UserSubscription, SubscriptionPack, Course

# import forms here
from .forms import UserLoginForm, UserRegisterForm

# SubscriptionPack Instance
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
        return redirect(home_view)
    context = {
        'form':form,
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
        user.save()
        #Subscription details of correspondance user
        userSub = UserSubscription(username=user, subscription_details=default_pack, subject_details=default_access)
        userSub.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        # Redirect to HOME-VIEW
        return redirect(profile_view)
    context = {
        'form':form,
        'layout': 1,
        'footer': 0,
    }
    return render(request, "accounts/signup.html", context)

def logout_view(request):
    logout(request)
    # Redirect to User-Login-Page
    return redirect('/')

@login_required
def home_view(request):
    context = {
        'layout': 1,
        'footer': 0,
    }
    return render(request, "accounts/home.html", context)

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

def template(request):
    return render(request, "accounts/template.html", {'value':1})

def mainTemp(request):
    return render(request, "accounts/main.html", {'footer':1, 'layout':0, })