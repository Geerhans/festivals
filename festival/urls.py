from django.urls import path
from festival import views

app_name = 'festival'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('festivalHistory/<slug:festival_name_slug>/', views.view_festivalHistory, name='festivalHistory'),
    path('shareStory/', views.view_shareStory, name='shareStory'),
    path('personalCenter/', views.personalCenter, name='personalCenter'),
    #path('logout/', views.user_logout, name='logout'),
    path('contactUs/', views.contactUs, name='contactUs'),
   #path('register/', views.register, name='register'),
   # path('login/', views.user_login, name='login'),
    path('country/<slug:country_name_slug>/', views.view_country, name='country'),

]
