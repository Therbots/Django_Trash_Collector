from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# TODO: Create an Employee model with properties required by the user stories

class Employee(models.Model):
    name = models.CharField(max_length=50, default="")
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name