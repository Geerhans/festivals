from operator import mod
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


#In the Festival project, there are a total of 3 models as follows:

#1.Country:Represents a country, and the fields have countryID, countryname, and slug.

#2.Festival：This project assumes that only the most unique festivals in the country 
# that are not found in other countries are listed. Therefore, the relationship 
# between countries and festivals is one-to-many.In the field of body shows the history
# of the festival.

#3.UserProfile:Display the attributes of the user. Its filed has user, website, picture.



class Country(models.Model):
    countryID = models.IntegerField(default=0)
    countryname = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(blank=True,unique=True)
    
    def save(self, *args, **kwargs):
        if self.countryID < 0:
            self.countryID = 0
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
    views = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)
    image_url=models.URLField(max_length=200,default="spring.jpg")

    def save(self, *args, **kwargs):
        if self.festivalID < 0:
            self.festivalID = 0
        self.slug = slugify(self.festivalname) 
        super(Festival, self).save(*args, **kwargs)

    def __str__(self): 
        return self.festivalname
    
    def get_absolute_url(self):
        return reverse('festival:view_shareStory', args=[self.id])




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username

