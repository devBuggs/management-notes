from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from accounts.models import UserSubscription

# Create your views here.

@login_required
def subject_view(request):
    currentUser = request.user
    subscription = UserSubscription.objects.get(username=currentUser.id)
    accessType = subscription.subscription_details
    subjectAccess = subscription.subject_details
    context = {
        'layout': 1,
        'footer': 0,
        'accessType': str(accessType),
        'subject': str(subjectAccess),
        #'navlink': subjectlink,
    }
    return render(request, "course/main.html", context)

