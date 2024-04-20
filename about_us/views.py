from django.shortcuts import render
from django.http import HttpResponse
from about_us.models import Teacher

# Create your views here.


def about_us(request):
    return render(request, 'about_us/about_us.html')


def teacher_info(request):
    info = Teacher.objects.all()
    context = {
        'info': info
    }
    return render(request, 'about_us/teachers.html', context)
