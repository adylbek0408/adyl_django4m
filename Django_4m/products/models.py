from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(null=True, blank=True)
    price = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    creadted_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
class Review_comm(models.Model):
    review = models.TextField()
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.review
