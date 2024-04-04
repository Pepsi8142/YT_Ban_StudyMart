from django.contrib import admin
from .models import Teachers

# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('t_id', 't_name', 't_email', 't_phone', 't_address')


admin.site.register(Teachers, TeacherAdmin)
