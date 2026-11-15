from django.db import models
from enum import Enum

# Create your models here.
class Concert(models.Model):
    class Meta:
        db_table = "concert"

class Producer(models.Model):
    class Meta:
        db_table = "producer"

class Setlist(models.Model):
    class Meta:
        db_table = "setlist"

class Song(models.Model):
    class Meta:
        db_table = "song"

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
        Chimera = "Chimera"
        Female = "Female"
        Male = "Male"

    gender = models.CharField(choices=Gender.choices, max_length=10)

    class Meta:
        db_table = "vocaloid"