from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    product = models.TextField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' ' + self.email + ' ' + self.address


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.TextField(max_length=100)
    title = models.CharField(max_length=50)
    is_suspended = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' ' + self.email + ' ' + self.address
