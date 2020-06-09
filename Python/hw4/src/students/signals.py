from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from students.models import Student


@receiver(pre_save, sender=Student)
def pre_save_student(sender, instance, **kwargs):
    instance.phone = ''.join(i for i in instance.phone if i.isdigit())

def pre_save_student_capitalize(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()

@receiver(post_save, sender=Student)
def post_save_student(sender, instance, **kwargs):
    print('post_save')