from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
# Create your views here.
from festival.models import Festival
from story.forms import StoryForm

#When we receive the transmitted festival_id, enter it into this 
# function to get the corresponding festival.

@login_required
def post_story(request, festival_id):
    festival = get_object_or_404(Festival, id=festival_id)

    if request.method == 'POST':
        story_form = StoryForm(request.POST)
        if story_form.is_valid():
            new_story = story_form.save(commit=False)
            new_story.festival = festival
            new_story.user = request.user
            new_story.save()
            return redirect(festival)
        else:
            return HttpResponse('There is fault.')
    else:
        return HttpResponse("Only accept post!")