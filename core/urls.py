from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="HOME"),
    path('shop', shop_page, name="shop_page"),
    path('search', search_product, name="search_product"),
    path('product-details/<slug:slug>', product_details, name="product_details"),
    path('about', about, name="about"),
    path('contact-us', contact_us, name="contact_us"),
    path('faq', faq, name="faq"),
    path('cart',cart,name="cart"),
    path('checkout',checkout,name="checkout"),
    path('add-to-cart/<int:id>', add_to_cart, name="ADD_TO_CART"),
    path('deleteCart/<int:id>', deleteCart, name="deleteCart"),
    path('order-page/<int:pk>',orderpage,name="orderpage"),
    path('invoice/<int:pk>',invoice,name="invoice"),
]
