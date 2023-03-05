from django.shortcuts import render
from .models import NFTImages,Invoice,User
from django.http import HttpResponse
import json


def home(request):
    products=NFTImages.objects.all()
    return render(request,'index.html',context={'products':products})