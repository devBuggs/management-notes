from django.contrib import admin

from .models import SubscriptionPack, User, UserDetail

# Register your models here.
admin.site.register(SubscriptionPack)
admin.site.register(User)
admin.site.register(UserDetail)