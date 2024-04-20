from django.db import models

# Create your models here.


class Teacher(models.Model):
    t_id = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    t_name = models.CharField(max_length=50)
    t_dob = models.DateField(null=True)
    t_email = models.EmailField(max_length=30, unique=True, null=True, blank=True)
    t_phone = models.CharField(null=True, blank=True, max_length=11, unique=True)
    t_address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.t_name
