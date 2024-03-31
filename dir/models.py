from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    dob = models.DateField()
    is_active = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'