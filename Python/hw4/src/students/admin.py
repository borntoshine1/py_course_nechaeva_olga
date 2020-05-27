from django.contrib import admin

from group.models import Group
from students.models import Student
from teachers.models import Teacher


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)


class GroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Group, GroupAdmin)


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)
