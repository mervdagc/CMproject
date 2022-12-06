from django.db import models


# Create your models here.

class Apimodel(models.Model):
    objects = None
    phone_number = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    operator = models.CharField(max_length=50)

    def __str__(self):
        return self.phone_number
