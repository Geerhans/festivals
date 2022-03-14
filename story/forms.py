from django import forms

from story.models import Story


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['body']