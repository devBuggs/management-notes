from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')

# Register your models here.
admin.site.register(Question, QuestionAdmin)