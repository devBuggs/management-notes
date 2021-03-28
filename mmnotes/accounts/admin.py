from django.contrib import admin

from .models import SubscriptionPack, UserSubscription, Course, LoggedInUser


# Register your models here.
admin.site.register(SubscriptionPack)
admin.site.register(UserSubscription)
admin.site.register(Course)
admin.site.register(LoggedInUser)