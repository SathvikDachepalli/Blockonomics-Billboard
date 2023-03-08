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
        invoice.save()

        user=User()
        if User.objects.filter(email=data['email']).exists():
            setof=User.objects.filter(email=data['email']).values('MoneySpent')
            add=0
            for x in setof:
                add+=x["MoneySpent"] 
            User.objects.filter(email=data['email']).update(MoneySpent=add+float(data['amount']))
            return HttpResponse("Success")


        user.username=data['name']
        user.email=data['email']
        user.MoneySpent=float(data['amount'])
        user.save()

        return HttpResponse("Success")
    name=None
    if Invoice.objects.filter(status=2).exists():
        filteredset=Invoice.objects.filter(status=2)

        getset={x['buyer']:[] for x in filteredset.values('buyer','price')}

        for x in filteredset.values('buyer','price'):
            getset[x['buyer']].append(x['price'])

        for x in getset:
            getset[x]=sum(getset[x])
        
        names=sorted(getset.items(), key=lambda x: x[1], reverse=True)
        print(names[0])
        
    return render(request,'index.html',context={'products':products,'data':data,'names':names})


