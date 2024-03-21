from django.db import models

# Create your models here.

# Department 
class Department(models.Model):
    DEPARTMENT_CHOICES = {
        ('HS', 'Home Science'),
        ('PA', 'Painting'),
        ('ENG', 'English'),
        ('DEO', 'Data Entry Operations'),
        ('BC', 'Basic Computing')
    }
    name = models.CharField(choices = DEPARTMENT_CHOICES, max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.get_name_display()} - {self.location}"

# Employee
class Employee(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete = models.CASCADE, null=False)

    def __str__(self):
        return f"{self.name}"