from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_01),
    path('forms/', views.show_form_data, name='show_form_data')
]
