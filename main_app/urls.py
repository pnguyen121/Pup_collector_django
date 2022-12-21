from django.urls import path
from . import views



urlpatterns = [
    # write path for the home page
    path('', views.home, name='home'),

    # write path for ABOUT page
    path('about/', views.about, name='about'),

    # writ path to view all pups
    path('pups/', views.pup_index, name='index')
]