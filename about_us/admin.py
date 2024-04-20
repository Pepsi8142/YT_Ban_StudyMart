from django.contrib import admin
from .models import Teacher

# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('t_id', 't_name', 't_email', 't_phone', 't_address')
# This class is used to make the data for the Model more readable under the admin panel.


admin.site.register(Teacher, TeacherAdmin)
