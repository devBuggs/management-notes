from django.db import models
from django.db.models import Q

from accounts.models import Course
'''
class SearchManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (
                Q(semester_name__icontains=query) |
                Q(subject_name__icontains=query) |
                Q(unit_name__icontains=query)
            )
            qs = qs.filter(or_lookup).distinct()
        return qs
'''

class SearchManager(models.Manager):
    def search(self, query=None, field=None):
        qs = self.get_queryset()
        if query is not None:
            if field == "semester_name":
                or_lookup = (Q(semester_name__icontains=query))
                print("----------------------------------> Serching in Semester Model")
            elif field == "subject_name":
                or_lookup = (Q(subject_name__icontains=query))
                print("----------------------------------> Serching in Subject Model")
            elif field == "unit_name":
                or_lookup = (Q(unit_name__icontains=query))
                print("----------------------------------> Serching in Unit Model")
            else:
                pass
            '''
            or_lookup = (
                Q(semester_name__icontains=query) |
                Q(subject_name__icontains=query) |
                Q(unit_name__icontains=query)
            )'''
            qs = qs.filter(or_lookup).distinct()
        return qs


# Create your models here.
class CourseSemester(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester_code = models.CharField(max_length=10, unique=True)
    semester_name = models.CharField(max_length=60)

    #objects = SearchManager()

    def __str__(self):
        return self.semester_code

class SemesterSubject(models.Model):
    semester_code = models.ForeignKey(CourseSemester, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=10, unique=True)

    objects = SearchManager()

    def __str__(self):
        return self.subject_code

class SubjectUnit(models.Model):
    subject_code = models.ForeignKey(SemesterSubject, on_delete=models.CASCADE)
    unit_name = models.CharField(max_length=100)
    unit_number = models.CharField(max_length=10)

    objects = SearchManager()

    def __str__(self):
        return self.unit_number
