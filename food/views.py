from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Item
from django.template import loader
# Create your views here.

def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list':item_list, 

    }
    return render(request, 'index.html', context)

def item(request):
    return HttpResponse("This is an item based view")

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item, 
    }
    return render(request, 'detail.html', context)

