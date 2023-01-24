from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)


class Review(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now=True)
    post = models.ForeignKey(Product, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
