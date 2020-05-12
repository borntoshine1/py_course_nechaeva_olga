# Generated by Django 2.2.12 on 2020-05-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(max_length=64)),
                ('course_name', models.CharField(max_length=64)),
                ('number_of_students', models.PositiveIntegerField()),
            ],
        ),
    ]
