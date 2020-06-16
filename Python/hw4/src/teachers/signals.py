from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from teachers.models import Teacher


@receiver(pre_save, sender=Teacher)
def pre_save_name_capitalize(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()

#@receiver(post_save, sender=Teacher)
#def post_save_teacher(sender, instance, **kwargs):