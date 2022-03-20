from django import forms

from story.models import Story

#Define a StoryForm for Story to submit the sent story
class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['body']