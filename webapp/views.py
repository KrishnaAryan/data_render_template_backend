from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):

    
    context ={'Frut' : Frut.objects.all()}

    return render(request, 'home.html',context)