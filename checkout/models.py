from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercart')


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitem')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    
