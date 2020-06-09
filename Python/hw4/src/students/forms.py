from django import forms

from students.models import Student


class StudentCreateForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'age',
            'phone',
            'password',
        )

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone.isdigit():
            raise forms.ValidationError(u"Passwords do not match.")
        cleaned_phone = ''.join(i for i in phone if i.isdigit())
        return cleaned_phone

    def clean(self):
        password = self.cleaned_data['password']
        password_repeat = self.cleaned_data['password_repeat']
        if password != password_repeat:
            raise forms.ValidationError(u"Passwords do not match.")
        return cleaned_data