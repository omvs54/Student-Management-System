from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'department', 'year', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter full name'}),
            'roll_no': forms.TextInput(attrs={'placeholder': 'Enter roll number'}),
            'department': forms.TextInput(attrs={'placeholder': 'Department'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Year'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
        }
    def clean_roll_no(self):
        roll_no = self.cleaned_data.get('roll_no')
        if Student.objects.filter(roll_no=roll_no).exists():
            raise forms.ValidationError("Roll number already exists.")
        return roll_no  