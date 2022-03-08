from operator import mod
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


# Create your models here.

class Country(models.Model):


    countryID = models.IntegerField(default=0)
    countryname = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.countryname) 
        super(Country, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Countries'
    
    def __str__(self):
        return self.countryname

    

class Festival(models.Model):


    festivalID = models.IntegerField(default=0)
    countryname = models.ForeignKey(Country, on_delete=models.CASCADE)
    festivalname = models.CharField(max_length=128)
    body = models.TextField()
    #image = models.ImageField()
    views = models.IntegerField(default=0)

    
    class Meta:
        verbose_name_plural = 'Festivals'

    def __str__(self): 
        return self.festivalname



class Story(models.Model):
    storyID = models.IntegerField(unique=True)
    
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
        ordering = ('datePosted',)
        verbose_name_plural = 'Stories'


class Comment(models.Model):
    commentID = models.IntegerField(unique=True)
    StoryID = models.ForeignKey(Story, on_delete=models.CASCADE)
  #  userID = models.ForeignKey(User)
# need a user foreignkey
    commentMessage = models.TextField()
    datePosted = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('datePosted',)
        verbose_name_plural = 'Comments'
    def __str__(self):
        return self.body[:20]

