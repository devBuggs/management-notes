from django.db import models
from django.contrib.auth.models import User


# Create your models here.
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
    subscription_details = models.OneToOneField(SubscriptionPack, on_delete=models.CASCADE)
    subject_details = models.OneToOneField(Course, on_delete=models.CASCADE)
    