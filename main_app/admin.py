from django.contrib import admin
# add Feeding to the import
from .models import Pup, Feeding

admin.site.register(Pup)
# register the new Feeding Model 
admin.site.register(Feeding)