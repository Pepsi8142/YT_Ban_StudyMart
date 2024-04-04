from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def machine_learning(request):
    course = 'machine learning'
    total_class = 21
    seat = 20
    course_duration = '2.5 months'
    context = {
        'course': course,
        'tc': total_class,
        'seat': seat,
        'cd': course_duration,
    }
    return render(request, 'machine_learning/machine_learning.html', context)


def decision_tree(request):
    teachers = {
        'names': ['Shakil', 'Mejbah', 'Sohan']
    }
    return render(request, 'machine_learning/decision_tree.html', context=teachers)


def knn(request):
    return render(request, 'machine_learning/knn.html')


def random_forest(request):
    return render(request, 'machine_learning/random_forest.html')


