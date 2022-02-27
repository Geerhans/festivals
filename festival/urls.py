from django.urls import path
from festival import views

app_name = 'shareStory'

urlpatterns = [
path('', views.index, name='index'),
]
