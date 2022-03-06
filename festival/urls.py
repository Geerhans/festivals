from django.urls import path
from festival import views

app_name = 'festival'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('festivalHistory/', views.festivalHistory, name='festivalHistory'),
    path('shareStory/', views.shareStory, name='shareStory'),
    path('personalCenter/', views.personalCenter, name='personalCenter'),
    path('shareStory/', views.shareStory, name='shareStory'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('signup/', views.signUp, name='signUp'),
    path('contactUs/', views.contactUs, name='contactUs'),
]
