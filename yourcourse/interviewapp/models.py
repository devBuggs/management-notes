from django.db import models



# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField(blank=True)

    def __str__(self):
        return self.question