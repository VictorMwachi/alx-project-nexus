from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def product_list(request):
    # This is a placeholder view function.
    # You can replace this with actual logic to fetch and display products.
    dummy_products = [
        {'name': 'Product 1', 'description': 'Description of Product 1'},
        {'name': 'Product 2', 'description': 'Description of Product 2'},
    ]
    return JsonResponse({'products': dummy_products})
