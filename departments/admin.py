from django.contrib import admin
from .models import Department, Rank, Employee

admin.site.register(Department)
admin.site.register(Rank)
admin.site.register(Employee)