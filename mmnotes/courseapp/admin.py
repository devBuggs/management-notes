from django.contrib import admin

from .models import CourseSemester, SemesterSubject, SubjectUnit

class CourseSemesterAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'semester_code', 'semester_name')
    list_filter = ['course_name']

class SemesterSubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_code', 'subject_name', 'semester_code')
    list_filter = ['semester_code']

class SubjectUnitAdmin(admin.ModelAdmin):
    list_display = ('unit_number', 'unit_name', 'subject_code')
    list_filter = ['subject_code']

# Register your models here.
admin.site.register(CourseSemester, CourseSemesterAdmin)
admin.site.register(SemesterSubject, SemesterSubjectAdmin)
admin.site.register(SubjectUnit, SubjectUnitAdmin)