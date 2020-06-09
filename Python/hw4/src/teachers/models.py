from django.db import models

# Create your models here.


class Teacher(models.Model):
    age = models.PositiveSmallIntegerField()
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    number_of_hours = models.PositiveSmallIntegerField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def info(self):
        return f'{self.id} {self.first_name} {self.last_name} {self.age} '

    def __str__(self):
        return self.info()
