from django.shortcuts import render
from django.http import HttpResponse
from .forms import TeacherRegistrationForm

# Create your views here.


def blog_01(request):
    return render(request, "blog/blog.html")


def show_form_data(request):
    if request.method == 'POST':
        data = TeacherRegistrationForm(request.POST)
        if data.is_valid():
            print(data.cleaned_data['password'])
            print(data.cleaned_data['repeat_password'])
    else:
        data = TeacherRegistrationForm()
    context = {
        'form': data
    }
    return render(request, "blog/forms.html", context)
