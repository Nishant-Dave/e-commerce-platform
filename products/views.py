from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse
# Create your views here..


def get_product(request, slug):
    try:

        product = get_object_or_404(Product, slug=slug)
        
        # Fetch all images related to the product
        images = product.images.all()
        
        # Fetch the price for the product (assuming you want the first available price)
        product_price = product.product_price.first()  # Adjust this as needed

        context = {
            'product': product,
            'images': images,
            'product_price': product_price
        }
        
        return render(request, 'product/product.html', context=context)
    
    except Product.DoesNotExist:
        return HttpResponse("Product not found", status=404)
    except Exception as e:
        print(f"An error occurred: {e}")
        return HttpResponse("An unexpected error occurred.", status=500)




# def get_product(request, slug):
#     product = None
#     try:
#         product = get_object_or_404(Product, slug=slug)
#         # product = Product.objects.get(slug = slug)
#         context = {
#             'product': product,
#             'images': product.images.all()
#                    }
        
#         # size = request.GET.get('size')             

#         return render(request, 'product/product.html', context=context)
    
#     except Product.DoesNotExist:
        
#         return HttpResponse("Product not found", status=404)
#     except Exception as e:
#         print (e)



# def get_product(request, slug):
#     # Fetch the product using the slug
#     product = get_object_or_404(Product, slug=slug)
    
#     # Pass the product to the template
#     return render(request, 'product/product.html', {'product': product})
