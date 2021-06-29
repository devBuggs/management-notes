from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse

class SearchManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query))
            qs = qs.filter(or_lookup).distinct()
        return qs

# Create your models here.
#CustonSessionModel
class LoggedInUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='logged_in_user', on_delete=models.CASCADE)
    # Session keys are 32 characters long
    session_key = models.CharField(max_length=32, blank=True, null=True)
 
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    objects = SearchManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('userDashboard') # redirecting to user_dashboard

class SubscriptionPack(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.CharField(max_length=50)

    def __str__(self):
        return self.subscription

class UserSubscription(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(SubscriptionPack, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
class UserContact(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=13)

    def __str__(self):
        return self.contact_number
