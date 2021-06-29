from django.db import models
from django.db.models import Q
from django.urls import reverse

# import models here
from accounts.models import Course

# ceate your custom managers here
class SearchManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query))
            qs = qs.filter(or_lookup).distinct()
        return qs

# create your models here
class CourseSemester(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    code = models.CharField(max_length=10, unique=True)

    objects = SearchManager()

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('sem', kwargs={'semester_code': str(self.code)})

class SemesterSubject(models.Model):
    semester_code = models.ForeignKey(CourseSemester, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    objects = SearchManager()

    def __str__(self):
        return self.name

    def get_semester_code(self):
        #print("----------------->>>>> ", self.semester_code.code)
        return self.semester_code.code
        
    def get_absolute_url(self):
        print(str(self.semester_code))
        return reverse('sub', kwargs={'semesterID': self.get_semester_code(), 'subjectID': str(self.code)})

class SubjectUnit(models.Model):
    subject_code = models.ForeignKey(SemesterSubject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    unit_number = models.CharField(max_length=10)

    objects = SearchManager() 

    def __str__(self):
        return self.name

    def get_semester_code(self):
        #print("----------------->>>>> ", self.subject_code.semester_code.code)
        return self.subject_code.semester_code.code

    def get_subject_code(self):
        #print("----------------->>>>> ", self.subject_code.code)
        return self.subject_code.code

    def get_absolute_url(self):
        return reverse('unitid', kwargs={'semesterID': self.get_semester_code(), 'subjectID': self.get_subject_code(), 'unit_code': str(self.unit_number)})

