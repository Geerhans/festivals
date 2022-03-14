from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
# Create your views here.
from festival.models import Festival
from story.forms import StoryForm


@login_required #(login_url='/userprofile/login/')
def post_story(request, festival_id):
   # try:
   #     festival = Festival.objects.get(id=festival_id) 
   # except Festival.DoesNotExist:
     #   festival = None
    # You cannot add a page to a Category that does not exist...
    festival = get_object_or_404(Festival, id=festival_id)
   # if festival is None:
    #    return redirect('/festival/')

    # POST
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