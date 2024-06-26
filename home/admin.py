from django.contrib import admin
from .models import Category,ProductImages,Products
# Register your models here.
admin.site.register(Products)
admin.site.register(ProductImages)
admin.site.register(Category)