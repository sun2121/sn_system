from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length=30,unique=True)
    spwd = models.CharField(max_length=30)


