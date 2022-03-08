from operator import mod
from django.db import models

from django.utils import timezone

# Create your models here.

class Country(models.Model):
    countryID = models.IntegerField(max_length=128,default=0)
    countryname = models.CharField(max_length=128, unique=True)
    
    class Meta:
        verbose_name_plural = 'Countries'
    
    def __str__(self):
        return self.countryname

    

class Festival(models.Model):
    countryname = models.ForeignKey(Country, on_delete=models.CASCADE)
    festivalID = models.IntegerField(max_length=128,default=0)
    festivalname = models.CharField(max_length=128)
    body = models.TextField()
    #image = models.ImageField()

    
    class Meta:
        verbose_name_plural = 'Festivals'

    def __str__(self): 
        return self.festivalname