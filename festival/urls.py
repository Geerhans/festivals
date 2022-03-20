from django.urls import path
from festival import views

app_name = 'festival'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('festivalHistory/<slug:festival_name_slug>/', views.view_festivalHistory, name='view_festivalHistory'),
    path('festivalHistory/', views.view_festivalHistory, name='festivalHistory'),
    path('shareStory/<int:id>/', views.view_shareStory, name='view_shareStory'),
    path('personalCenter/', views.personalCenter, name='personalCenter'),
    path('country/<slug:country_name_slug>/', views.view_country, name='view_country'),

]
