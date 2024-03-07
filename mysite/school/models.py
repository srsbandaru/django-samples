from django.db import models

# Create your models here.

# School
class School(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    yearOfEstablishment = models.PositiveIntegerField()
    email = models.EmailField(max_length=200) 
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
# Student
class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, on_delete = models.CASCADE, null=False)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
