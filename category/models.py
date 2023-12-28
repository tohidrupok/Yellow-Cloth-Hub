from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length= 100, unique = True)
    description = models.TextField(max_length = 255, null = True) 
    cat_image = models.ImageField(upload_to = 'photos/categories', null = True)
    
    def __str__(self):
        return self.category_name 
    
    
class Brand(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length= 100, unique = True) 
    
    def __str__(self):
        return self.category_name 
        
class SELLER(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length= 100, unique = True)
    description = models.TextField(max_length = 255, null = True) 
    
    def __str__(self):
        return self.category_name 
    

class PRODUCT_BY(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length= 100, unique = True)
    description = models.TextField(max_length = 255, null = True) 
    
    def __str__(self):
        return self.category_name 
    
class warranty_period(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length= 100, unique = True)
    description = models.TextField(max_length = 255, null = True) 
    
    def __str__(self):
        return self.category_name 