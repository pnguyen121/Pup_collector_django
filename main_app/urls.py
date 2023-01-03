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
    path('pups/<int:pup_id>/add_feeding', views.add_feeding, name='add_feeding'),

    # associate a toy with a cat (M:M)
  path('pups/<int:pup_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),

# TOY STUFF
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),

]