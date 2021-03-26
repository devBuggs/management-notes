from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login, logout

from .forms import UserLoginForm, UserRegisterForm
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
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        # Redirect to HOME-VIEW
        return redirect(home_view)
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
    context = {
        'layout': 0,
        'footer': 1,
    }
    return render(request, "accounts/profile.html", context)

def template(request):
    return render(request, "accounts/template.html", {'value':1})

def mainTemp(request):
    return render(request, "accounts/main.html", {'footer':1, 'layout':0, })