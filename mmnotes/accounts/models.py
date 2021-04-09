from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

#CustonSessionModel
class LoggedInUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='logged_in_user', on_delete=models.CASCADE)
    session_key = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Course(models.Model):
    course = models.CharField(max_length=50)
    
    def __str__(self):
        return self.course

class SubscriptionPack(models.Model):
    subscription = models.CharField(max_length=20)

    def __str__(self):
        return self.subscription

class UserSubscription(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription_details = models.ForeignKey(SubscriptionPack, on_delete=models.CASCADE)
    subject_details = models.ForeignKey(Course, on_delete=models.CASCADE)
    

class UserContact(models.Model):
    username = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=13)

    def __str__(self):
        return self.contact_number