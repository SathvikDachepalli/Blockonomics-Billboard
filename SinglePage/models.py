from django.db import models

class NFTImages(models.Model):
    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    productId=models.AutoField(primary_key=True)
    price = models.FloatField()
    description = models.TextField()
    def __str__(self):
        return self.title

class Invoice(models.Model):
    status_choices=((-1,"Not Started"),(0,"Not confirmed"),(1,"Processing"),(2,"Paid"))

    image=models.ForeignKey(NFTImages,on_delete=models.CASCADE)
    invoiceId=models.AutoField(primary_key=True)
    productId=models.IntegerField()
    address=models.CharField(max_length=250)
    buyer=models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateField()
    status=models.IntegerField(choices=status_choices,default=-1)
    def __str__(self):
        return self.address

class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100, blank=False, null=False)
    email=models.EmailField(max_length=254,default="example@gmail.com",blank=False, null=False)
    MoneySpent=models.FloatField(default=0,blank=False, null=False)
    def __str__(self):
        return self.username