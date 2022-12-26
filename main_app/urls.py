from django.urls import path
from . import views




urlpatterns = [
    # write path for the home page
    path('', views.home, name='home'),

    # write path for ABOUT page
    path('about/', views.about, name='about'),

    # writ path to view all pups
    path('pups/', views.pups_index, name='index'),

    path('pups/<int:pup_id>/', views.pups_detail, name='detail'),

    # new route usedd to show aa form to create a pup
    path('pups/create/', views.PupCreate.as_view(), name='pups_create'),

    # edit/upddate route
    path('pups/<int:pk>/update/', views.PupUpdate.as_view(), name='pups_update'),

    # delete route
    path('pups/<int:pk>/delete/', views.PupDelete.as_view(), name='pups_delete'),

    #path for the feeding form
    path('pups/<int:pup_id>/add_feeding', views.add_feeding, name='add_feeding')

]