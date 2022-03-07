from django.urls import path
from festival import views

app_name = 'festival'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('festivalHistory/', views.festivalHistory, name='festivalHistory'),
    path('shareStory/', views.shareStory, name='shareStory'),
    path('personalCenter/', views.personalCenter, name='personalCenter'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('signup/', views.signUp, name='signUp'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('india/', views.India, name='India'),
    path('UK/', views.UK, name='UK'),
    path('USA/', views.USA, name='USA'),
    path('italy/', views.Italy, name='Italy'),
    path('china/', views.China, name='China'),
]
