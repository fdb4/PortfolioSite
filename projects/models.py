from django.db import models

# Create your models here.
class Projectshort(models.Model):
    title = models.CharField(max_length=75)
    description=models.TextField()

class Projectlong(models.Model):
    title = models.CharField(max_length=75)
    description=models.TextField()
    url=models.URLField()
    highlight1 = models.CharField(max_length=150, blank=True)
    highlight2 = models.CharField(max_length=150, blank=True)
    highlight3 = models.CharField(max_length=150, blank=True)
    highlight4 = models.CharField(max_length=150, blank=True)
    highlight5 = models.CharField(max_length=150, blank=True)