from django.shortcuts import render
from .models import Produits

# Create your views here.


def home(request):
    return render(request, 'home_template.html')


def produits(request):
    all_fields = Produits._meta.get_fields()
    context = {'champs_liste' : all_fields[1:3]}
    
        
    return render(request, 'produits_template.html', context)