from django.db import models

# Create your models here.

class Teacher(models.Model):
    full_name = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    number_of_hours = models.FloatField()
