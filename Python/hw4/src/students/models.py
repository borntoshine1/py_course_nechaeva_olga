from django.db import models


# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=24, default='')
    password = models.CharField(max_length=128, default='')

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def info(self):
        return f'{self.id} {self.first_name} {self.last_name} {self.age} '

    def __str__(self):
        return self.info()
