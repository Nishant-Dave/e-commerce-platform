from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse
# Create your views here..


def get_product(request, slug):
    product = None
    try:
        product = get_object_or_404(Product, slug=slug)
        # product = Product.objects.get(slug = slug)
        context = {'product': product}

        print(f"Product retrieved: {product}")

        size = request.GET.get('size') 
        if size:
            # size = request.GET.get('size')
            price = product.get_product_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price

            print(f"Size: {size}, Price: {price}")
            

        return render(request, 'product/product.html', context=context)
    
    except Product.DoesNotExist:
        # Handle the case where the product does not exist
        return HttpResponse("Product not found", status=404)
    except Exception as e:
        print (e)