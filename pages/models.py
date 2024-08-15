from django.db import models
# Create your models here.
class Aboutme(models.Model):
    name = models.CharField(max_length=150)
    aboutme=models.TextField()
    linkedinurl=models.CharField(max_length=200)
    githuburl=models.CharField(max_length=200)
class Education(models.Model):
    school=models.CharField(max_length=150)
    degree=models.CharField(max_length=150)
    major = models.CharField(max_length=150)
    minor=models.CharField(max_length=150)
    startyear=models.CharField(max_length=200)
    stopyear=models.CharField(max_length=200)
class Coreskills(models.Model):
    skill=models.CharField(max_length=150)
class Certifications(models.Model):
    name = models.CharField(max_length=150)
    certgot = models.CharField(max_length=150)
    expir = models.CharField(max_length=150)
class Workexperience(models.Model):
    name = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    starty= models.CharField(max_length=150)
    endy = models.CharField(max_length=150)
    highlight1 = models.CharField(max_length=150, blank=True)
    highlight2 = models.CharField(max_length=150, blank=True)
    highlight3 = models.CharField(max_length=150, blank=True)
    highlight4 = models.CharField(max_length=150, blank=True)