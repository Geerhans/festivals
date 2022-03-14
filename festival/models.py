from operator import mod
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Country(models.Model):
    countryID = models.IntegerField(default=0)
    countryname = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(blank=True,unique=True)
    
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
    slug = models.SlugField(blank=True)
    image_url=models.URLField(max_length=200,default="spring.jpg")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.festivalname) 
        super(Festival, self).save(*args, **kwargs)

    def __str__(self): 
        return self.festivalname
    
    def get_absolute_url(self):
        return reverse('festival:view_shareStory', args=[self.id])



class Story(models.Model):
    storyID = models.IntegerField(unique=True)
    
    festivalID = models.ForeignKey(Festival, on_delete=models.CASCADE)
 #   userID = models.ForeignKey(User)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username

