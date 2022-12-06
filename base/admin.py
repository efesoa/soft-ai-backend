from django.contrib import admin
from .models import Client, Employee

admin.site.register([Client, Employee])
