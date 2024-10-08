from django.db import models
from base.models import BaseModel
from django.utils.text import slugify



class Category(BaseModel):
    category_name = models.CharField(max_length=50)
    category_img = models.ImageField(upload_to='categories')
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name

class ColorVariant(BaseModel):
    color_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.color_name

class RAM(BaseModel):
    size_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.size_name

class Product(BaseModel):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_description = models.TextField(blank=True, null=True)
    color_variant = models.ManyToManyField(ColorVariant, blank=True)
    ram_variant = models.ManyToManyField(RAM, blank=True)

    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.product_name

    # def get_product_price_by_size(self, size):
    #     return self.price + SizeVariant.objects.get(size_name = size).price

class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_price')
    ram = models.ForeignKey('RAM', on_delete=models.CASCADE)
    color = models.ForeignKey('ColorVariant', on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.product.product_name} - {self.ram} - {self.color} - ${self.price}"



class ProductImg(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    color = models.ForeignKey(ColorVariant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return f"{self.product.product_name} - {self.color.color_name}"
    

class Coupon(BaseModel):
    coupon_code = models.CharField(max_length=10)
    is_expired = models.BooleanField(default=False)
    discount_price = models.IntegerField(default=100)
    minimum_amount = models.IntegerField(default=500)

    def __str__(self) -> str:
        return self.coupon_code
    

