from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

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


def index(request):

    return render(request, 'index1.html')


def create_teacher(request):
    from teachers.forms import TeacherCreateForm

    if request.GET:
        form = TeacherCreateForm(request.GET)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TeacherCreateForm(request.GET)

    context = {'create_form': form}

    return render(request, 'create_teachers.html', context=context)
