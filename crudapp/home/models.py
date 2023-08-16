from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=10)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
