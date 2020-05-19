from django import forms

from group.models import Group


class GroupCreateForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = (
            'teacher',
            'course_name',
            'number_of_students',
        )
