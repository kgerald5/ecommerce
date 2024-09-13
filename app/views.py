from django.shortcuts import render
from django.views.generic import View
from .models import Product


def base(request, *args, **kwargs):
    return render(request, "app/base.html", {})

def home(request, *args, **kwargs):  # Correction du nom de la vue
    return render(request, "app/home.html", {})

class CategoryView(View):
 def get(self, request, val):
        product=Product.objects.filter(category=val) 
        return render(request, "app/category.html", locals())
        title=Product.objects.filter(category=val).values('title')