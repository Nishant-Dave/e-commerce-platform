from django.shortcuts import render, get_object_or_404
from .models import Product, ProductPrice
from django.http import HttpResponse


def get_product(request, slug):
    try:

        product = get_object_or_404(Product, slug=slug)
        product_price = product.product_price.all()  

        # price_dict = {
        #     f"{price.ram.id}-{price.color.id}": price.price for price in product_price
        # }
        price_dict = {}
        for price in product_price:
        # Since ram is a ForeignKey, we can directly access its id
            price_dict[f"{price.ram.uid}-{price.color.uid}"] = price.price


        context = {
            'product': product,
            'product_price': product_price,
            'price_dict': price_dict
        }
        print(f"The product dict is:  {price_dict}")
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
