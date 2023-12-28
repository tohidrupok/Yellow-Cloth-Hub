from django.db import models
from category.models import Category , PRODUCT_BY , SELLER , warranty_period
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True) 
    Product = models.ForeignKey(PRODUCT_BY, on_delete=models.CASCADE)
    Warranty = models.ForeignKey(warranty_period, on_delete=models.CASCADE)
    Seller = models.ForeignKey(SELLER, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.product_name 
    

