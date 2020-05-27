from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt # noqa imported but unused
from django.template import RequestContext # noqa imported but unused


from faker import Faker

from teachers.forms import TeacherCreateForm
from teachers.models import Teacher

# Create your views here.


def teachers(request):
    teachers_query = Teacher.objects.all()

    params = [
        'age',
        'first_name',
        'last_name',
        'id',
        'subject',
        'number_of_hours',
    ]

    for param in params:
        value = request.GET.get(param)
        if value:
            teachers_query = teachers_query.filter(**{param: value})

    return render(request, 'teachers-list.html', context={'teachers': teachers_query})


def index(request):

    return render(request, 'index_tch.html')


def create_teacher(request):

    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))
    elif request.method == 'GET':
        form = TeacherCreateForm()

    context = {'create_form': form}

    return render(request, 'create_teacher.html', context=context)


def edit_teacher(request, pk):

    teacher = get_object_or_404(Teacher, id=pk)

    if request.method == 'POST':
        form = TeacherCreateForm(request.POST, instance=teacher)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))
    elif request.method == 'GET':
        form = TeacherCreateForm(instance=teacher)

    context = {'form': form, 'id': teacher.id}

    return render(request, 'edit_tch.html', context=context)


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    teacher.delete()
    return HttpResponseRedirect(reverse('teachers:list'))


def generate(count):
    fake = Faker()
    lst_teachers = []
    for i in range(int(count)):
        lst_teachers.append(
            Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=fake.pyint(20, 90, 1),
                subject=fake.job(),
                number_of_hours=fake.pyint(0, 100, 1)))

    return lst_teachers
