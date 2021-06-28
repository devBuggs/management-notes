from django.contrib import admin

# Import models here.
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('made_by', 'order_id', 'made_on')
    list_filter = ['made_on']

# Register your models here.
admin.site.register(Transaction, TransactionAdmin)