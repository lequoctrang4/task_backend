from django.db import models
# Create your models here.

class Category(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

class Product(models.Model):
    # id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    style = models.CharField(max_length=200)
    pattern = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    climate = models.CharField(max_length=200)
    publish_date = models.DateField()
    quantity = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, auto_created=True)
    
class DetailProduct(models.Model):
    # id = models.IntegerField(primary_key=True)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.IntegerField()
    sale_price = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, auto_created=True)

class ImageProduct(models.Model):
    # id = models.IntegerField(primary_key=True)
    # image = models.ImageField(upload_to='images/')
    image = models.TextField()
    detail_product_id = models.ForeignKey(Product, on_delete=models.CASCADE, auto_created=True)