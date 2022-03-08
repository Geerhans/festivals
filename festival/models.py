from operator import mod
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

from django.utils import timezone

# Create your models here.
#class User(models.Model):


class Country(models.Model):

    countryID = models.IntegerField(max_length=128, unique=True)
    countryname = models.CharField(max_length=128)
    slug = models.SlugField()
    def save(self, *args, **kwargs):
        self.slug = slugify(self.countryname) 
        super(Country, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Countries'
    
    def __str__(self):
        return self.countryname

    

class Festival(models.Model):

    festivalID = models.IntegerField(max_length=128, unique=True)
    countryID = models.ManyToManyField(Country, on_delete=models.CASCADE)
    festivalname = models.CharField(max_length=128)
    body = models.TextField()
    #image = models.ImageField()
    views = models.IntegerField(default=0)
    slug = models.SlugField()
    def save(self, *args, **kwargs):
        self.slug = slugify(self.festivalname) 
        super(Festival, self).save(*args, **kwargs)

    
    class Meta:
        verbose_name_plural = 'Festivals'

    def __str__(self): 
        return self.festivalname


class Story(models.Model):
    storyID = models.IntegerField(max_length=128, unique=True)
    
    festivalID = models.ForeignKey(Festival, on_delete=models.CASCADE)
 #   userID = models.ForeignKey(User)
# need a user foreignkey
    storyMessage = models.TextField()
    datePosted = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
   # slug = models.SlugField()
   # def save(self, *args, **kwargs):
   #     self.slug = slugify(self.countryname) 
   #     super(Country, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)
        verbose_name_plural = 'Stories'


class Comment(models.Model):
    commentID = models.IntegerField(max_length=128, unique=True)
    StoryID = models.ForeignKey(Story, on_delete=models.CASCADE)
  #  userID = models.ForeignKey(User)
# need a user foreignkey
    commentMessage = models.TextField()
    datePosted = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
        verbose_name_plural = 'Comments'
    def __str__(self):
        return self.body[:20]

