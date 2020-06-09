from django.core.management.base import BaseCommand # noqa imported but unused

from faker import Faker

from students.models import Student


class Command(BaseCommand):
    help = 'Generate random students' # noqa is a python builtin

    def add_arguments(self, parser):
        parser.add_argument('value', nargs='?', type=int, help='Value students', default=100)

    def handle(self, *args, **kwargs):
        value = kwargs['value']
        fake = Faker()
        students = []
        for _ in range(value):
            students.append(Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=fake.pyint(20, 90, 1),
            ))
        Student.objects.bulk_create(students)
