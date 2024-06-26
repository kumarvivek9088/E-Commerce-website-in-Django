from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self',null=True,blank=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.name} - {self.id}'
    
class ProductImages(models.Model):
    image = models.ImageField(upload_to='product_images/')
    image1 = models.ImageField(upload_to='product_images/',null=True,blank=True)
    image2 = models.ImageField(upload_to='product_images/',null=True,blank=True)
    image3 = models.ImageField(upload_to='product_images/',null=True,blank=True)


class Products(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField()
    stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    images = models.ForeignKey(ProductImages,on_delete=models.SET_NULL,null=True)
    # added_at = 
    