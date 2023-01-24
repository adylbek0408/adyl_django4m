from django.contrib import admin
from products.models import Product, Review_comm, Category

# Register your models here.

admin.site.register(Product)
admin.site.register(Review_comm)
admin.site.register(Category)
