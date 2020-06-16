# Generated by Django 2.2.12 on 2020-06-09 12:01

from django.db import migrations

#from students.models import Student


def forwards(apps, schema):
    Student = apps.get_model('students', 'Student')

    def full_name(instance):
        return f"{instance.first_name} {instance.last_name}"

    def info(instance):
        return f'{instance.id} {instance.first_name} {instance.last_name} {instance.age} '

    for student in Student.objects.all().only('phone').iterator():
        student.phone = ''.join(i for i in student.phone if i.isdigit())
        student.save(update_fields=['phone'])

    for student in Student.objects.all().only('first_name').iterator():
        student.first_name = student.first_name.capitalize()
        student.save(update_fields=['first_name'])

    for student in Student.objects.all().only('last_name').iterator():
        student.last_name = student.last_name.capitalize()
        student.save(update_fields=['last_name'])

#def backwards(apps, schema):
    #print('forwards')


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_password'),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]
