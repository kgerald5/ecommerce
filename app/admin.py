from django.contrib import admin

# Register your models here.
from . models import Product

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
 list_display=['id', 'title', 'discounted_price', 'category', 'product_image']
