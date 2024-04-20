from django import forms
import email
from django.core import validators


class TeacherRegistrationForm(forms.Form):
    first_name = forms.CharField(label='Enter your First name')
    last_name = forms.CharField(label='Enter your Last name')
    date_of_birth = forms.DateField(label='Enter your Date of Birth', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(label='Choose your Gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], required=False)
    subject = forms.CharField(label='What is your subject?', required=False)
    experience = forms.CharField(label='Describe your experience', widget=forms.Textarea, required=False)
    job_category = forms.ChoiceField(label='Choose your job category', required=False, choices=[('FT', 'Full Time'), ('PT', 'Part Time'), ('C', 'Contractual')])
    photo = forms.ImageField(label='Upload your photo', required=False, widget=forms.FileInput)
    email = forms.EmailField(label='Enter your Email')
    password = forms.CharField(label='Enter your password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Repeat your password', widget=forms.PasswordInput)
    agree = forms.BooleanField(label='Do you agree with our terms & condition?', required=True, widget=forms.CheckboxInput, initial=False)

    def clean(self):
        cleaned_data = super().clean()
        right_pass = self.cleaned_data['password']
        wrong_pass = self.cleaned_data['repeat_password']
        if right_pass != wrong_pass:
            raise forms.ValidationError('Passwords do not match')

    # class Meta:
    #     fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'gender', 'subject', 'address', 'city']
