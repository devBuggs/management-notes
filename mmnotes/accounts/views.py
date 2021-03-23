from django.shortcuts import render

# Create your views here.

def login_view(request):
    #if request.method == 'POST':
        # Instanciate Login Form
        # Validate Loin Form
            #check form data validation
        #if validation failed raise error
    return render(request, "account/login.html", context=None)

def register_view(request):
    return render(request, "account/register.html", context=None)