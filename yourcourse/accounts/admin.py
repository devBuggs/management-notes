from django.contrib import admin

from .models import SubscriptionPack, UserSubscription, Course, LoggedInUser, UserContact

class UserContactAdmin(admin.ModelAdmin):
    list_display = ('username', 'contact_number')

class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('username', 'subscription', 'course')
    list_filter = ['subscription', 'course']

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')

class SubscriptionPackAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscription')

class LoggedInUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_key')

# Register your models here
#admin.site.register(SubscriptionPack, SubscriptionPackAdmin)
admin.site.register(UserSubscription, UserSubscriptionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(LoggedInUser, LoggedInUserAdmin)
admin.site.register(UserContact, UserContactAdmin)
