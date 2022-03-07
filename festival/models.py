from operator import mod
from django.db import models

from django.utils import timezone

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=128, unique=True)
    
    class Meta:
        verbose_name_plural = 'Countries'
    
    def __str__(self):
        return self.name

    

class Festival(models.Model):
    country = models.ManyToManyField(Country)
    title = models.CharField(max_length=128)
    body = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Festivals'

    def __str__(self): 
        return self.title


class Story(models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
# need a user foreignkey
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
        verbose_name_plural = 'Stories'

class Comment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comment')
# need a user foreignkey
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('created',)
        verbose_name_plural = 'Comments'
    def __str__(self):
        return self.body[:20]
