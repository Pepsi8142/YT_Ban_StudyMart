from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('t_info', views.teacher_info, name='t_info'),

]