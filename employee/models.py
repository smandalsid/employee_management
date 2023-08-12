from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    emp_id=models.CharField(max_length=6)
    emp_dept=models.CharField(max_length=100, null=True)
    desig=models.CharField(max_length=100, null=True)
    contact=models.CharField(max_length=10, null=True)
    gender=models.CharField(max_length=10, null=True)
    join_date=models.DateField(null=True)

    def __str__(self):
        return self.user.username