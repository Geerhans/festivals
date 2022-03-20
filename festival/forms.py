from django import forms 
from django.contrib.auth.models import User 
from festival.models import UserProfile


#In the forms.py module, we need define several classes that inherit 
# from ModelForm ModelForm is a helper class provided by Django that 
# simplifies the process of creating forms for models. There are now 
# two models in the user profile (User and UserProfile) for which we 
# need define subclasses of ModelForm for each.

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta: 
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm): 
    class Meta:
        model = UserProfile
        fields = ('picture',)