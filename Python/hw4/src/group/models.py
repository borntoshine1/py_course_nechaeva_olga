from django.db import models

# Create your models here.

class Group(models.Model):
    teacher = models.CharField(max_length=64)
    course_name = models.CharField(max_length=64)
    number_of_students = models.PositiveIntegerField()
