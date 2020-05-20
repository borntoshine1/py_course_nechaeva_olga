from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render # noqa imported but unused
from django.urls import reverse

from faker import Faker

from students.models import Student


# Create your views here.

def index(request):

    return render(request, 'index_st.html')


def students(request):
    count = Student.objects.count()
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
    from students.forms import StudentCreateForm

    if request.method == 'POST':
        form = StudentCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    elif request.method == 'GET':
        form = StudentCreateForm()

    context = {'create_form': form}

    return render(request, 'create_students.html', context=context)


def edit_students(request):
    from students.forms import StudentCreateForm

    student = Student.objects.first()

    if request.method == 'POST':
        form = StudentCreateForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    elif request.method == 'GET':
        form = StudentCreateForm(instance=student)

    context = {'form': form}

    return render(request, 'edit.html', context=context)


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
