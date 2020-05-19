from django.core.management.base import BaseCommand # noqa imported but unused

from faker import Faker

from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generate random teachers' # noqa is a python builtin

    def add_arguments(self, parser):
        parser.add_argument('value', nargs='?', type=int, help='Value teachers', default=100)

    def handle(self, *args, **kwargs):
        value = kwargs['value']
        fake = Faker()
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=fake.pyint(20, 90, 1),
            number_of_hours=fake.pyint(0, 200, 1),
            subject=fake.license_plate()
        )
        for _ in range(value):
            Teacher.objects.bulk_create([teacher])
