from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.TextField(max_length=200)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):                  # to get the name attribute of the instance.
        return self.name

