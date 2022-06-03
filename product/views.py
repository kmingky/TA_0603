from django.shortcuts import render
from .models import Category, Drink

# Create your views here.

def Select_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        pass