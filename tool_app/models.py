from django.db import models
from .models import *

# Create your models here.
class user(models.Model):
    user = models.AutoField(primary_key=True)
    user_firstname = models.CharField(max_length=50)
    user_lastname = models.CharField(max_length=50)
    user_gender = models.CharField(max_length=10)
    user_tel = models.CharField(max_length=10)

    def __str__(self):
        return f'{self._firstname} {self.user_lastname}'