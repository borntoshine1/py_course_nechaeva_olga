from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext # noqa imported but unused


from faker import Faker

from students.forms import StudentCreateForm
from students.models import Student


def index(request):

    return render(request, 'index_st.html')


def students(request):
    students_query = Student.objects.all()

    params = [
        'age',
        'first_name',
        'last_name',
        'id',
    ]

    for param in params:
        value = request.GET.get(param)
        if value:
            students_query = students_query.filter(**{param: value})

    return render(request, 'students-list.html', context={'students': students_query})


def create_students(request):

    if request.method == 'POST':
        form = StudentCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    elif request.method == 'GET':
        form = StudentCreateForm()

    context = {'create_form': form}

    return render(request, 'create_students.html', context=context)


@csrf_exempt
def edit_students(request, pk):

    student = get_object_or_404(Student, id=pk)

    if request.method == 'POST':
        form = StudentCreateForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    elif request.method == 'GET':
        form = StudentCreateForm(instance=student)

    context = {'form': form, 'id': student.id}

    return render(request, 'edit.html', context=context)


def delete_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    return HttpResponseRedirect(reverse('students:list'))


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
