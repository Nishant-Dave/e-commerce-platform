from django.contrib import admin
from django.utils.text import slugify
from .models import *

class RAMInline(admin.TabularInline):
    model = Product.ram_variant.through  
    extra = 1

class ColorVariantInline(admin.TabularInline):
    model = Product.color_variant.through  
    extra = 1

class ProductPriceInline(admin.TabularInline):
    model = ProductPrice
    extra = 1

class ProductImageAdmin(admin.TabularInline):  
    model = ProductImg
    list_display = ['product', 'color']  
    extra = 1 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category']
    inlines = [RAMInline, ColorVariantInline, ProductPriceInline, ProductImageAdmin]

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.product_name)
        super().save_model(request, obj, form, change)

@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color_name']

@admin.register(RAM)
class RAMAdmin(admin.ModelAdmin):
    list_display = ['size_name']

@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ['product', 'ram', 'color', 'price']
    search_fields = ['product__product_name', 'ram__size_name', 'color__color_name']  

admin.site.register(Category)
admin.site.register(Coupon)
admin.site.register(ProductImg)




# from django.contrib import admin
# from .models import *
# from django.contrib.admin import StackedInline

# # Register your models here.

# admin.site.register(Category)
# admin.site.register(Coupon)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductImg)


# class ProductImageAdmin(admin.StackedInline):
#     model = ProductImg

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['product_name', 'price', ]
#     inlines = [ProductImageAdmin]

# @admin.register(ColorVariant)
# class ColorVariantAdmin(admin.ModelAdmin):
#     list_display = ['color_name', 'price']
#     model = ColorVariant

# @admin.register(RAM)
# class SizeVariantAdmin(admin.ModelAdmin):
#     list_display = ['size_name', 'price']
#     model = RAM


# from django.contrib import admin
# from .models import *

# # Register your models here.

# admin.site.register(Category)
# admin.site.register(Coupon)
# admin.site.register(ProductImg)

# # Inline for linking Product with RAM variants
# class RAMInline(admin.TabularInline):
#     model = Product.ram_variant.through  # Linking RAM variants to Product
#     extra = 1

# # Inline for linking Product with Color variants
# class ColorVariantInline(admin.TabularInline):
#     model = Product.color_variant.through  # Linking Color variants to Product
#     extra = 1

# # Inline for managing price for each combination of Product + RAM + Color
# class ProductRAMColorPriceInline(admin.TabularInline):
#     model = ProductRAMColorPrice  # Inline for the ProductRAMColorPrice model
#     extra = 1

# # Admin for managing Products
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['product_name', 'category']  # Removed price as it's now in ProductRAMColorPrice
#     inlines = [ProductImageAdmin, RAMInline, ColorVariantInline, ProductRAMColorPriceInline]

#     def save_model(self, request, obj, form, change):
#         obj.slug = slugify(obj.product_name)
#         super().save_model(request, obj, form, change)

# # Admin for managing Color variants
# @admin.register(ColorVariant)
# class ColorVariantAdmin(admin.ModelAdmin):
#     list_display = ['color_name']  # Removed price as it's now in ProductRAMColorPrice
#     model = ColorVariant

# # Admin for managing RAM variants
# @admin.register(RAM)
# class RAMAdmin(admin.ModelAdmin):
#     list_display = ['size_name']  # Removed price as it's now in ProductRAMColorPrice
#     model = RAM

# # Admin for managing the price of each combination of Product + RAM + Color
# @admin.register(ProductRAMColorPrice)
# class ProductRAMColorPriceAdmin(admin.ModelAdmin):
#     list_display = ['product', 'ram', 'color', 'price']
#     search_fields = ['product__product_name', 'ram__size_name', 'color__color_name']

# # Register the Product model with the custom ProductAdmin
# admin.site.register(Product, ProductAdmin)



# from django.contrib import admin
# from django.utils.text import slugify
# from .models import *

# class RAMInline(admin.TabularInline):
#     model = Product.ram_variant.through  
#     extra = 1

# class ColorVariantInline(admin.TabularInline):
#     model = Product.color_variant.through  
#     extra = 1


# class ProductPriceInline(admin.TabularInline):
#     model = ProductPrice
#     extra = 1


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['product_name', 'category']  
#     inlines = [RAMInline, ColorVariantInline, ProductPriceInline]

#     def save_model(self, request, obj, form, change):
#         obj.slug = slugify(obj.product_name)
#         super().save_model(request, obj, form, change)


# @admin.register(ColorVariant)
# class ColorVariantAdmin(admin.ModelAdmin):
#     list_display = ['color_name']


# @admin.register(RAM)
# class RAMAdmin(admin.ModelAdmin):
#     list_display = ['size_name']


# @admin.register(ProductPrice)
# class ProductPriceAdmin(admin.ModelAdmin):
#     list_display = ['product', 'ram', 'color', 'price']
#     # search_fields = ['product__product_name', 'ram__size_name', 'color__color_name']


# class ProductImageAdmin(admin.TabularInline):  
#     model = ProductImg
#     extra = 1 

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ProductImageAdmin]
#     list_display = ['product_name']


# # Register other models
# admin.site.register(Category)
# admin.site.register(Coupon)
# admin.site.register(ProductImg)

# # Register the Product model with the custom ProductAdmin
# admin.site.register(Product, ProductAdmin)
