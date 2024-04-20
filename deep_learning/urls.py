from django.urls import path
from . import views

urlpatterns = [
    path('', views.deep_learning),
    path('register/', views.registration, name='register'),

]
