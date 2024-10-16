from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import Cart, CartItem
from products.models import Product, ProductPrice, RAM, ColorVariant
from django.http import HttpResponse, HttpResponseRedirect


def get_product(request, slug):
    try:

        product = get_object_or_404(Product, slug=slug)
        product_price = product.product_price.all()  

        # price_dict = {
        #     f"{price.ram.id}-{price.color.id}": price.price for price in product_price
        # }
        price_dict = {}
        for price in product_price:

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



def add_to_cart(request, uid):
    product = get_object_or_404(Product, uid=uid)
    user = request.user
    
    # Get or create the cart for the user
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
    
    # Create a new CartItem for the product
    cart_item = CartItem.objects.create(cart=cart, product=product)
    
    # Check if the request contains a RAM variant and color option
    ram_variant_id = request.GET.get('select_ram')
    color_variant_id = request.GET.get('select_color')

    if ram_variant_id:
        try:
            ram_variant = RAM.objects.get(uid=ram_variant_id)  # Assuming RAM is identified by a UID
            cart_item.ram_variant = ram_variant
        except RAM.DoesNotExist:
            print(f"RAM variant with UID {ram_variant_id} does not exist")
    
    if color_variant_id:
        try:
            color_variant = ColorVariant.objects.get(uid=color_variant_id)  # Assuming ColorVariant is also identified by UID
            cart_item.color_variant = color_variant
        except ColorVariant.DoesNotExist:
            print(f"Color variant with UID {color_variant_id} does not exist")

    # Save the cart item
    cart_item.save()

    # Redirect back to the same page or a cart summary page
    return HttpResponseRedirect(request.path_info)



# def add_to_cart(request, uid):
    
#     variant = request.GET.get('variant')
#     product = get_object_or_404(Product, uid=uid)
#     user = request.user
#     cart, _ = Cart.object.get_or_create(user = user, is_paid = False)
#     cart_item = CartItem.objects.create(cart = cart, product = product)

#     if variant:
#         variant = request.GET.get('variant')
#         ram_variant = RAM.objects.get(ram_variant = variant)
#         cart_item.ram_variant = ram_variant
#         cart_item.save()

#     return HttpResponseRedirect(request.path_info)



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
