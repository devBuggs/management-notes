from django.db import models

from accounts.models import Course

# Create your models here.


class CourseSemester(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester_code = models.CharField(max_length=10, unique=True)
    semester_name = models.CharField(max_length=60)

    def __str__(self):
        return self.semester_code

class SemesterSubject(models.Model):
    semester_code = models.ForeignKey(CourseSemester, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return str(self.subject_code) + " - " + str(self.subject_name)

class SubjectUnit(models.Model):
    subject_code = models.ForeignKey(SemesterSubject, on_delete=models.CASCADE)
    unit_name = models.CharField(max_length=100)
    unit_number = models.CharField(max_length=10)

    def __str__(self):
        return str(self.subject_code) + " / " + str(self.unit_number)
