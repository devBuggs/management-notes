from django.contrib import admin

from .models import SubscriptionPack, UserSubscription, Course, LoggedInUser, UserContact


class UserContactAdmin(admin.ModelAdmin):
    list_display = ('username', 'contact_number')

class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('username', 'subscription_details', 'subject_details')
    list_filter = ['subscription_details', 'subject_details']

# Register your models here.
admin.site.register(SubscriptionPack)
admin.site.register(UserSubscription, UserSubscriptionAdmin)
admin.site.register(Course)
admin.site.register(LoggedInUser)
admin.site.register(UserContact, UserContactAdmin)
