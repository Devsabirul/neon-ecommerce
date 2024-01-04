from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="HOME"),
    path('shop', shop_page, name="shop_page"),
    path('product-details/<slug:slug>', product_details, name="product_details"),
    path('about', about, name="about"),
    path('cart',cart,name="cart"),
    path('add-to-cart/<int:id>', add_to_cart, name="ADD_TO_CART"),
    path('deleteCart/<int:id>', deleteCart, name="deleteCart"),
]
