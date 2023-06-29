from django.shortcuts import render
from django.http import HttpResponse

# Creation du template 
def index(request):
    return render(request, 'produits/index.html')