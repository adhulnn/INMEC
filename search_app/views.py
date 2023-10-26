from django.shortcuts import render
from shop.models import Product
from django.db.models import Q


# Create your views here.
def search_result(req):
    products = None
    query = None

    if 'q' in req.GET:
        query = req.GET.get('q')
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    print(f"Query: {query}")
    print(f"Number of products: {products.count()}")

    return render(req, 'search.html', {'query': query, 'products': products})
