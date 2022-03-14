from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from festival.models import Festival


class Story(models.Model):
    festival = models.ForeignKey(
        Festival,
        on_delete=models.CASCADE,
        related_name='stories',
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='stories',
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created',)
        
    def __str__(self):
        return self.body[:20]