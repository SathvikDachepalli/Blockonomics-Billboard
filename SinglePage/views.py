from django.shortcuts import render
from .models import NFTImages,Invoice,User
from django.http import HttpResponse
import json
from datetime import datetime


def home(request):
    print(request.method)
    products=NFTImages.objects.all().values()
    data=request.POST
    print(data)
    if request.method == "POST" and 'pk' in request.POST:
        data = request.POST
        invoice=Invoice()
        invoice.image=NFTImages.objects.get(productId=data['pk'])
        invoice.productId=data['pk']
        invoice.address=data['email']
        invoice.buyer=data['name']
        invoice.price=data['amount']
        invoice.date=datetime.today()
        invoice.status=0
        # invoice.save()

        user=User()
        user.username=data['name']
        user.email=data['email']
        setof=User.objects.filter(email=data['email']).values('MoneySpent')
        sum=0
        for x in setof:
            sum+=x["MoneySpent"] 
        print(sum)
        # # previous_purchase=0 if user.MoneySpent==None else User.objects.get(email=data['email']).MoneySpent
        user.MoneySpent=data['amount']
        # user.save()

        print(data)

        return HttpResponse("Success")
    
    return render(request,'index.html',context={'products':products,'data':data})


# <QueryDict: {'pk': ['1'], 'amount': ['66.4'], 'email': ['dachepallisathvik@gmail.com'], 
# 'name': ['Sathvik'], 
# 'csrfmiddlewaretoken': ['t3R6IQJozpf12BsGpDqhYIQRrNnyDT2HBL2e7Rw6MSbtNKhPAYtfMBmyGC64Cpvg']}>