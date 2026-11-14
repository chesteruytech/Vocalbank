from django.db import models
from enum import Enum

# Create your models here.
# class Concert(models.Model):

# class Producer(models.Model):

# class Setlist(models.Model):

# class Song(models.Model):

class VOCALOIDGender(Enum):
    c = "Chimera"
    f = "Female"
    m = "Male"

class VOCALOID(models.Model):
    vocaloid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    language = models.CharField(max_length=75)
    releaseDate = models.DateField()

    class Gender(models.TextChoices):
        c = "Chimera"
        f = "Female"
        m = "Male"

    role = models.CharField(choices=Gender.choices, max_length=10)