from django.http import HttpResponse
from django.shortcuts import render # noqa imported unused

from teachers.models import Teacher

# Create your views here.


def teachers(request):
    teachers_filter = Teacher.objects.all()

    age = request.GET.get('age')
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')

    teachers_filter = Teacher.objects.all()

    if age:
        teachers_filter = teachers_filter.filter(age=age)

    if first_name:
        teachers_filter = teachers_filter.filter(first_name=first_name)

    if last_name:
        teachers_filter = teachers_filter.filter(last_name=last_name)

    response = f'teachers: {teachers_filter.count()}<br/>'

    for teacher in teachers_filter:
        response += teacher.info() + '<br/>'

        return HttpResponse(response)
