from django.http import HttpResponse
from django.shortcuts import render # noqa imported but unused

from faker import Faker

from students.models import Student


# Create your views here.

def students(request):
    count = Student.objects.count()
    students_query = Student.objects.all()

    response = f'students:  {count}<br/>'

    for student in students_query:
        response += student.info() + '<br/>'

    return HttpResponse(response)


def random_student(request):
    # noqa student = Student.objects.create(first_name=fake.first_name(), last_name=fake.last_name(), age=fake.pyint(20, 90, 1))
    lst_students = generate(1)
    response = f'student - {lst_students[0].info()} <br/>'

    return HttpResponse(f' {response}')


def hundred_students(request):

    count = request.GET['count']

    if count.isdigit() is False:
        return HttpResponse(f"Error: must be an integer")
    if int(count) <= 0:
        return HttpResponse(f"Error: count must be greater than zero")

    if int(count) > 100:
        return HttpResponse(f"Error: count must be less than a hundred")

    lst_students = generate(count)
    response = ''
    for student in lst_students:
        response += student.info() + '<br/>'

    return HttpResponse(f' {response} ')


def generate(count):
    fake = Faker()
    lst_students = []
    for i in range(int(count)):
        lst_students.append(
            Student.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=fake.pyint(0, 90, 1)))

    return lst_students
