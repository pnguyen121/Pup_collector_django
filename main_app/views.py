from django.shortcuts import render, redirect
# import our CBV thing
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
# import in our model
from .models import Pup
# import the feeding form
from .forms import FeedingForm

# Create your views here.

# DELETE PUP HERE USEING THE CVB STUFF we imported all the CBV stuff above which
# Does the heavy lifting for us.
# in order for this to work we need a confirm delete template


class PupDelete(DeleteView):
    model = Pup
    # redirect to view all pups page
    success_url = '/pups/'


# UPDATE PUP HERE!!
class PupUpdate(UpdateView):
    model = Pup
    fields = ['breed', 'description', 'age']


# CREATE NEW PUP HERE
class PupCreate(CreateView):
    # takes our Pup model from models
    model = Pup
    # the form field we includde all from the models two underscores __all__
    fields = '__all__'

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

# Update the detials page with the feeding stuff


def pups_detail(request, pup_id):
    pup = Pup.objects.get(id=pup_id)
    # set the feeding form to
    feeding_form = FeedingForm()
    return render(request, 'pups/detail.html', {'pup': pup, 'feeding_form': feeding_form})


def add_feeding(request, pup_id):
    form = FeedingForm(request.POST)
    # Validate the form
    if form.is_valid():
        # dont save the form to the DB until it has the pup_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.pup_id = pup_id
        new_feeding.save()
        # alwaays redirect when changing the database and import redirect at the top
    return redirect('detail', pup_id=pup_id)
