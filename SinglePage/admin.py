from django.contrib import admin
from .models import *


class NFTImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'productId', 'price', 'description')

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('image', 'invoiceId', 'productId', 'address', 'buyer', 'price', 'date', 'status')

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'MoneySpent')

admin.site.register(NFTImages, NFTImagesAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(User, UserAdmin)
