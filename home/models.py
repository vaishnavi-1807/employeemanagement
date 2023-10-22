from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=5, unique=True)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=10)

    def _str_(self):
        return self.first_name + ' ' + self.last_name