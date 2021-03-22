from django.db import models

# Create your models here.

class SubscriptionPack(models.Model):
    subscription = models.CharField(max_length=100)

    def __str__(self):
        return self.subscription

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=24)

    def __str__(self):
        return self.email

class UserDetail(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(SubscriptionPack, on_delete=models.CASCADE)
