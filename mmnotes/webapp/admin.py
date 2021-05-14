from django.contrib import admin

from .models import contact, ClientReview

class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')

class ClientReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

# Register your models here.
admin.site.register(contact, contactAdmin)
admin.site.register(ClientReview, ClientReviewAdmin)