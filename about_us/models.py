from django.db import models

# Create your models here.


class Teachers(models.Model):
    t_id = models.IntegerField(primary_key=True)
    t_name = models.CharField(max_length=50)
    t_email = models.EmailField(max_length=30, unique=True, null=True, blank=True)
    t_phone = models.IntegerField(null=True, blank=True)
    t_address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.t_name
