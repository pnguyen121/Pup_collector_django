from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


# Fake data used here:
class Pup:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

pups = [
  Pup ('Benji', 'Corgi', 'Young King', 2),
  Pup ('Dash', 'Mini Golden Doodle', 'Pup that pees in the house when excitedd', 1),
  Pup ('Indy', 'Long Hair Mini Dachshund', 'Long hair dont care', 1)
]





# Write the functions that match the path in the urls.py


# home function connects to urls.py
def home(request):
    return render(request, 'home.html')

# about function connects to urls.py
def about(request):
    return render(request, 'about.html')

# all pups function 
def pup_index(request):
    return render(request, 'pups/index.html', {'pups': pups})
