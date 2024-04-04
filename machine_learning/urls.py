from django.urls import path
from . import views

urlpatterns = [
    path('', views.machine_learning),
    path('dt/', views.decision_tree),
    path('knn/', views.knn, name='knn'),
    path('rf/', views.random_forest),
]
