# Generated by Django 2.2.12 on 2020-06-09 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='', max_length=128),
        ),
    ]
