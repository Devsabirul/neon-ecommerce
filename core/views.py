from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.http import JsonResponse


def home(request):
    cart = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    popularpd = PopularDepartMents.objects.all()
    products = Products.objects.order_by("-id")
    context = {
        'navbar':'home',
        'popularDepartment':popularpd,
        'cart':cart,
        'products':products
    }
    return render(request,'core/index.html',context)


def shop_page(request):
    cart = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    products = Products.objects.order_by("-id")
    context = {
        'navbar':'shop',
        'products':products,
        'cart':cart
    }
    return render(request,"core/shop.html",context)

def product_details(request,slug):
    cart = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        cart_quantity = Cart.objects.get(user=request.user,product__slug=slug)
        
        if request.method == "POST":
            productid = request.POST.get('productId')
            quantitys = request.POST.get('quantity')
            quantity_ = int(quantitys)
            product_ = int(productid)
            if quantity_ != 0:
                try:
                    cart = Cart.objects.get(Q(product=product_,user = request.user))
                    print(cart)
                    cart.quantity = quantity_
                    cart.save()
                except Cart.DoesNotExist:
                    Cart(user=request.user,product=product,quantity=quantity_).save()
                return JsonResponse({'status': 'success'})
    product = Products.objects.get(slug=slug)
    context = {
        'navbar':'shop',
        'product':product,
        'cart':cart,
        'cart_quantity':cart_quantity
    }
    return render(request,"core/product_details.html",context)

def about(request):
    cart = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    return render(request,"core/about.html",{'navbar':'about','cart':cart})

def cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        subtotal = get_subTotal(cart)  

        if request.method == "POST":
            cartId = request.POST.get('cartId')
            quantitys = request.POST.get('quantity')
            quantity_ = int(quantitys)
            cartID = int(cartId)
            if quantity_ != 0:
                try:
                    cart = Cart.objects.get(Q(id=cartID,user = request.user))
                    cart.quantity = quantity_
                    cart.save()
                    line_total = cart.line_total
                    
                except Cart.DoesNotExist:
                    Cart(user=request.user,product=product,quantity=quantity_).save()
                return JsonResponse({'status': 'success'})

        return render(request,"core/cart.html",locals())
    else:
        return redirect("login")

def add_to_cart(request,id):
    if request.user.is_authenticated:
        product = Products.objects.get(id=id)
        quantity_ = 1
        try:
            cart = Cart.objects.get(Q(product=product,user = request.user))
            cart.quantity += 1
            cart.save()
        except Cart.DoesNotExist:
            Cart(user=request.user,product=product,quantity=quantity_).save()
        return redirect('shop_page')
    else:
        return redirect('login')

def deleteCart(request,id):
    if request.user.is_authenticated:
        print(id)
        cart = Cart.objects.get(Q(user=request.user,id=id))
        print(cart)
        cart.delete()
        return redirect('cart')



# custom function 
def get_subTotal(carts):
    cartTotals = []
    for cart in carts:
        subtotal  = cart.product.price*cart.quantity
        cartTotals.append(subtotal)
    return sum(cartTotals)


def carts(request):
    if request.user.is_authenticated:
        try:
            carts = Cart.objects.filter(user=request.user)
            subtotal = get_subTotal(carts)
            return {'carts':carts,'subtotal':subtotal}
        except Exception as e:
            pass