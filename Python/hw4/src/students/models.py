from django.db import models


# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveIntegerField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def info(self):
        return f'{self.id} {self.first_name} {self.last_name} {self.age} '


class Group(models.Model):
    classroom = models.CharField(max_length=64)
    course_name = models.CharField(max_length=64)
    number_of_students = models.PositiveIntegerField()

class Teacher(models.Model):
    full_name = models.CharField(max_length=64)
    number_of_hours = models.FloatField()
    

     
    
