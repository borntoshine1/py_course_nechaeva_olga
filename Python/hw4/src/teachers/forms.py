from django import forms

from teachers.models import Teacher


class TeacherCreateForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = (
            'first_name',
            'last_name',
            'age',
            'subject',
            'number_of_hours'
        )


    def capitalize_first_name(self):
        first_name = self.cleaned_data['first_name']
        cleaned_name = first_name.capitalize()
        return cleaned_name


    def capitalize_last_name(self):
        last_name = self.cleaned_data['last_name']
        cleaned_name = last_name.capitalize()
        return cleaned_name