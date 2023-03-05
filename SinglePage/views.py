from django.shortcuts import render
from .models import NFTImages,Invoice,User
from django.http import HttpResponse
import json



def home(request):
    print(request.method)
    if request.method == "POST":
        data = request.POST
        print(data)
    products=NFTImages.objects.all().values()
    return render(request,'index.html',context={'products':products})


