from django.contrib import admin



from .models import CourseSemester, SemesterSubject, SubjectUnit

# Register your models here.
admin.site.register(CourseSemester)
admin.site.register(SemesterSubject)
admin.site.register(SubjectUnit)