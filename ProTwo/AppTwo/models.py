from django.db import models

# Create your models here.
class User(models.Model):
    FirstName = models.CharField(max_length=128)
    LastName = models.CharField(max_length=128)
    Email = models.CharField(max_length=264,unique = True)
