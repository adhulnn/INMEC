from django.shortcuts import render,get_object_or_404
from .models import Category,Product

# Create your views here.
def allCat(req,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products=Product.objects.all().filter(category=c_page,available=True)
    else:
        products=Product.objects.all().filter(available=True)
    return render(req,'category.html',{'category':c_page,'products':products})

def proDetail(req,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(req,'product.html',{'product':product})