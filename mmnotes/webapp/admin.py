from django.contrib import admin

from .models import contact

class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')

# Register your models here.
admin.site.register(contact, contactAdmin)