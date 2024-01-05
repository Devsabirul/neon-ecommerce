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

def contact_us(request):
    cart = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    return render(request,"core/contact_us.html",{'navbar':'contact_us','cart':cart})

def faq(request):
    cart = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    return render(request,"core/faq.html",{'navbar':'faq','cart':cart})

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
        cart = Cart.objects.get(Q(user=request.user,id=id))
        cart.delete()
        return redirect('cart')


def checkout(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        subtotal = get_subTotal(cart)
        if request.method == "POST":
            frist_name = request.POST.get("firstname")
            last_name = request.POST.get("lastname")
            company_name = request.POST.get("company-name")
            country = request.POST.get("country-name")
            address = request.POST.get("street")
            city = request.POST.get("town")
            zipcode = request.POST.get("zip")
            state = request.POST.get("state")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            customer = Customer(country=country,first_name=frist_name,last_name=last_name,company_name=company_name,Address=address,city=city,state=state,zipcode=zipcode,email=email,phone=phone,user=request.user)
            customer.save()
            # order press 
            customer_ = Customer.objects.order_by("-id")[:1].get()
            order = Order(customer=customer_, user=request.user, total_order=subtotal)
            order.save()
            order_ = Order.objects.order_by("-id")[:1].get()
            for i in cart:
                OrderItems(order=order_, product=i.product,
                            quantity=i.quantity, user=request.user).save()
            return redirect("orderpage",pk=order_.id)
        return render(request,"core/checkout.html",locals())
    else:
        return redirect("login")


def orderpage(request,pk):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        order = Order.objects.get(user=request.user,id=pk)
        orderitems = OrderItems.objects.filter(user=request.user,order=order)
        return render(request,"core/order.html",locals())
    else:
        return redirect("login")

def invoice(request,pk):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        order = Order.objects.get(user=request.user,id=pk)
        orderitems = OrderItems.objects.filter(user=request.user,order=order)
        return render(request,"core/invoice.html",locals())
    else:
        return redirect("login")


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