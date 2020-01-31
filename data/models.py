from django.db import models

# Create your models here.

class Gsm(models.Model):
    #latitude = models.CharField(max_length = 200)
    #longitude = models.CharField(max_length = 200)
    latitude=models.DecimalField(max_digits=12, decimal_places=6)
    longitude=models.DecimalField(max_digits=12, decimal_places=6)
    name = models.CharField(max_length = 20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
