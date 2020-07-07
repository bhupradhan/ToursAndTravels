from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
#from .models import Destination
# Create your views here.
from .models import Domestic


def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html") 

def domestic(request):
    data = Domestic.objects.all()
    return render(request, "domestic.html",{'data': data})       


