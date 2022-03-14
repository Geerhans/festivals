

from django.urls import path
from . import views

app_name = 'story'

urlpatterns = [
    path('post_story/<int:festival_id>/', views.post_story, name='post_story'),

]