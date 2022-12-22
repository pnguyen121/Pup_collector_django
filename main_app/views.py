from django.shortcuts import render

from django.http import HttpResponse

# import in our model
from .models import Pup

# Create your views here.


# Write the functions that match the path in the urls.py

# home function connects to urls.py
def home(request):
    return render(request, 'home.html')

# about function connects to urls.py
def about(request):
    return render(request, 'about.html')

# all pups function 
def pups_index(request):
    pups = Pup.objects.all()
    return render(request, 'pups/index.html', {'pups': pups})

def pups_detail(request, pup_id):
    pup = Pup.objects.get(id=pup_id)
    return render(request, 'pups/detail.html', {'pup': pup})
