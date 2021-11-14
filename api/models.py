from django.db import models

# Create your models here.
class Url(models.Model):
    long = models.CharField(max_length=1000, blank=False, unique=True)
    short = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.long