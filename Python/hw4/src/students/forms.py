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
        if phone.isdigit() != True:
            raise forms.ValidationError(u"Phone do not match.")
        cleaned_phone = ''.join(i for i in phone if i.isdigit())
        return cleaned_phone


    def capitalize_first_name(self):
        first_name = self.cleaned_data['first_name']
        cleaned_name = first_name.capitalize()
        return cleaned_name


    def capitalize_last_name(self):
        last_name = self.cleaned_data['last_name']
        cleaned_name = last_name.capitalize()
        return cleaned_name
    
