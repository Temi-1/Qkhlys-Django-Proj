from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=23)
    address = models.CharField(max_length=23)
    
    def __str__(self) -> str:
        return self.name 

class City(models.Model):
    name = models.CharField(max_length=23)

    def __str__(self) -> str:
        return self.name 