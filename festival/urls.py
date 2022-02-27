from django.urls import path
from festival import views

app_name = 'shareFestival'

urlpatterns = [
path('', views.index, name='index'),
]
