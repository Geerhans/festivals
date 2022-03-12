from django.urls import path
from festival import views

app_name = 'festival'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
   # path('festivalHistory/<festivalSlug:festival_name_slug>/', views.view_festivalHistory, name='festivalHistory'),
    path('festivalHistory/', views.view_festivalHistory, name='view_festivalHistory'),
    path('shareStory/', views.view_shareStory, name='view_shareStory'),
    path('personalCenter/', views.personalCenter, name='personalCenter'),
    #path('logout/', views.user_logout, name='logout'),
    path('contactUs/', views.contactUs, name='contactUs'),
   #path('register/', views.register, name='register'),
   # path('login/', views.user_login, name='login'),
    path('country/<slug:country_name_slug>/', views.view_country, name='view_country'),

]
