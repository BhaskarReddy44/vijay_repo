from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    sal=models.FloatField()
    eadd=models.CharField(max_length=45)