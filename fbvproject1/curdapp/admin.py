from django.contrib import admin
from curdapp.models import Employee
# Register your models here.
class EmployeeAdimin(admin.ModelAdmin):
    list_display = ['eno','ename','sal','eadd']

admin.site.register(Employee,EmployeeAdimin)