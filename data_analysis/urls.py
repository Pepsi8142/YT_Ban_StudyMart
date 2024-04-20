from django.urls import path
from . import views

urlpatterns = [
    path('function', views.data_analysis, name='function'),              # Function-based url
    path('class', views.DataAnalysis.as_view(), name='class'),           # Class-based url
]
