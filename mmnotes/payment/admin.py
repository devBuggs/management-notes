from django.contrib import admin


# Import models here.
from .models import Transaction


# Register your models here.
admin.site.register(Transaction)