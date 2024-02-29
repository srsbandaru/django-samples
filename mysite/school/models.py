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