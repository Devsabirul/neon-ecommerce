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
    sub_sub_category = SubSubCategory.objects.all()
    sub_category = SubCategory.objects.all()
    category = Category.objects.all()

    home_garden = []
    electronics = []
    fashion = []
    furniture = []
    healthy_beauty = []
    gift_ideas = []
    toy_games = []
    cooking = []
    smart_phones = []
    cameras_photo = []
    accessories = []


    for i in sub_category:
        if i.category.filtername == "home_&_garden":
            home_garden.append(i.name)
        elif i.category.filtername == "electronics":
            electronics.append(i.name)
        elif i.category.filtername == "fashion":
            fashion.append(i.name)
        elif i.category.filtername == "furniture":
            furniture.append(i.name)
        elif i.category.filtername == "healthy_&_beauty":
            healthy_beauty.append(i.name)
        elif i.category.filtername == "gift_ideas":
            gift_ideas.append(i.name)
        elif i.category.filtername == "toy_&_games":
            toy_games.append(i.name)
        elif i.category.filtername == "cooking":
            cooking.append(i.name)
        elif i.category.filtername == "smart_phones":
            smart_phones.append(i.name)
        elif i.category.filtername == "cameras_&_photo":
            cameras_photo.append(i.name)
        elif i.category.filtername == "accessories":
            accessories.append(i.name)



    context = {
        'navbar':'home',
        'popularDepartment':popularpd,
        'cart':cart,
        'products':products,
        'sub_sub_category':sub_sub_category,
        'sub_category':sub_category,
        'home_garden':home_garden,
        'electronics':electronics,
        'fashion':fashion,
        'furniture':furniture,
        'healthy_beauty':healthy_beauty,
        'gift_ideas':gift_ideas,
        'cooking':cooking,
        'smart_phones':smart_phones,
        'cameras_photo':cameras_photo,
        'accessories':accessories,
        'toy_games':toy_games,
        'category':category
    }
    return render(request,'core/index.html',context)


def shop_page(request):
    cart = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    products = Products.objects.order_by("-id")
    sub_sub_category = SubSubCategory.objects.all()
    sub_category = SubCategory.objects.all()
    category = Category.objects.all()
    category_ = request.GET.get("category")
    sub_category_ = request.GET.get("subcategory")
    category_product = []
    is_product = True
    

    if category_ != None:
        category_product = Products.objects.filter(category__filtername=category_)
        is_product = False
    
    if sub_category_ != None:
        category_product = Products.objects.filter(subcategory__name=sub_category_) 
        is_product = False

    home_garden = []
    electronics = []
    fashion = []
    furniture = []
    healthy_beauty = []
    gift_ideas = []
    toy_games = []
    cooking = []
    smart_phones = []
    cameras_photo = []
    accessories = []


    for i in sub_category:
        if i.category.filtername == "home_&_garden":
            home_garden.append(i.name)
        elif i.category.filtername == "electronics":
            electronics.append(i.name)
        elif i.category.filtername == "fashion":
            fashion.append(i.name)
        elif i.category.filtername == "furniture":
            furniture.append(i.name)
        elif i.category.filtername == "healthy_&_beauty":
            healthy_beauty.append(i.name)
        elif i.category.filtername == "gift_ideas":
            gift_ideas.append(i.name)
        elif i.category.filtername == "toy_&_games":
            toy_games.append(i.name)
        elif i.category.filtername == "cooking":
            cooking.append(i.name)
        elif i.category.filtername == "smart_phones":
            smart_phones.append(i.name)
        elif i.category.filtername == "cameras_&_photo":
            cameras_photo.append(i.name)
        elif i.category.filtername == "accessories":
            accessories.append(i.name)

    context = {
        'navbar':'shop',
        'products':products,
        'cart':cart,
        'sub_sub_category':sub_sub_category,
        'sub_category':sub_category,
        'home_garden':home_garden,
        'electronics':electronics,
        'fashion':fashion,
        'furniture':furniture,
        'healthy_beauty':healthy_beauty,
        'gift_ideas':gift_ideas,
        'cooking':cooking,
        'smart_phones':smart_phones,
        'cameras_photo':cameras_photo,
        'accessories':accessories,
        'toy_games':toy_games,
        'category_product':category_product,
        'is_product':is_product
    }
    return render(request,"core/shop.html",context)


def search_product(request):
    products = Products.objects.filter(name__icontains=request.GET.get('search'))

    sub_sub_category = SubSubCategory.objects.all()
    sub_category = SubCategory.objects.all()
    category = Category.objects.all()

    home_garden = []
    electronics = []
    fashion = []
    furniture = []
    healthy_beauty = []
    gift_ideas = []
    toy_games = []
    cooking = []
    smart_phones = []
    cameras_photo = []
    accessories = []


    for i in sub_category:
        if i.category.filtername == "home_&_garden":
            home_garden.append(i.name)
        elif i.category.filtername == "electronics":
            electronics.append(i.name)
        elif i.category.filtername == "fashion":
            fashion.append(i.name)
        elif i.category.filtername == "furniture":
            furniture.append(i.name)
        elif i.category.filtername == "healthy_&_beauty":
            healthy_beauty.append(i.name)
        elif i.category.filtername == "gift_ideas":
            gift_ideas.append(i.name)
        elif i.category.filtername == "toy_&_games":
            toy_games.append(i.name)
        elif i.category.filtername == "cooking":
            cooking.append(i.name)
        elif i.category.filtername == "smart_phones":
            smart_phones.append(i.name)
        elif i.category.filtername == "cameras_&_photo":
            cameras_photo.append(i.name)
        elif i.category.filtername == "accessories":
            accessories.append(i.name)

    return render(request,"core/search.html",locals())


def product_details(request,slug):
    cart = 0
    cart_quantity = 1
    product = Products.objects.get(slug=slug)
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        try:
            cart_quantity = Cart.objects.get(user=request.user,product__slug=slug)
            cart_quantity = cart_quantity.quantity
        except Cart.DoesNotExist:
            cart_quantity = 1
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

    sub_sub_category = SubSubCategory.objects.all()
    sub_category = SubCategory.objects.all()
    category = Category.objects.all()

    home_garden = []
    electronics = []
    fashion = []
    furniture = []
    healthy_beauty = []
    gift_ideas = []
    toy_games = []
    cooking = []
    smart_phones = []
    cameras_photo = []
    accessories = []


    for i in sub_category:
        if i.category.filtername == "home_&_garden":
            home_garden.append(i.name)
        elif i.category.filtername == "electronics":
            electronics.append(i.name)
        elif i.category.filtername == "fashion":
            fashion.append(i.name)
        elif i.category.filtername == "furniture":
            furniture.append(i.name)
        elif i.category.filtername == "healthy_&_beauty":
            healthy_beauty.append(i.name)
        elif i.category.filtername == "gift_ideas":
            gift_ideas.append(i.name)
        elif i.category.filtername == "toy_&_games":
            toy_games.append(i.name)
        elif i.category.filtername == "cooking":
            cooking.append(i.name)
        elif i.category.filtername == "smart_phones":
            smart_phones.append(i.name)
        elif i.category.filtername == "cameras_&_photo":
            cameras_photo.append(i.name)
        elif i.category.filtername == "accessories":
            accessories.append(i.name)

    context = {
        'navbar':'shop',
        'product':product,
        'cart':cart,
        'cart_quantity':cart_quantity,
        'sub_sub_category':sub_sub_category,
        'sub_category':sub_category,
        'home_garden':home_garden,
        'electronics':electronics,
        'fashion':fashion,
        'furniture':furniture,
        'healthy_beauty':healthy_beauty,
        'gift_ideas':gift_ideas,
        'cooking':cooking,
        'smart_phones':smart_phones,
        'cameras_photo':cameras_photo,
        'accessories':accessories,
        'toy_games':toy_games,
    }
    return render(request,"core/product_details.html",context)

def about(request):
    cart = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    
    sub_sub_category = SubSubCategory.objects.all()
    sub_category = SubCategory.objects.all()
    category = Category.objects.all()

    home_garden = []
    electronics = []
    fashion = []
    furniture = []
    healthy_beauty = []
    gift_ideas = []
    toy_games = []
    cooking = []
    smart_phones = []
    cameras_photo = []
    accessories = []


    for i in sub_category:
        if i.category.filtername == "home_&_garden":
            home_garden.append(i.name)
        elif i.category.filtername == "electronics":
            electronics.append(i.name)
        elif i.category.filtername == "fashion":
            fashion.append(i.name)
        elif i.category.filtername == "furniture":
            furniture.append(i.name)
        elif i.category.filtername == "healthy_&_beauty":
            healthy_beauty.append(i.name)
        elif i.category.filtername == "gift_ideas":
            gift_ideas.append(i.name)
        elif i.category.filtername == "toy_&_games":
            toy_games.append(i.name)
        elif i.category.filtername == "cooking":
            cooking.append(i.name)
        elif i.category.filtername == "smart_phones":
            smart_phones.append(i.name)
        elif i.category.filtername == "cameras_&_photo":
            cameras_photo.append(i.name)
        elif i.category.filtername == "accessories":
            accessories.append(i.name)

    context = {
        'navbar':'about',
        'cart':cart,
        'sub_sub_category':sub_sub_category,
        'sub_category':sub_category,
        'home_garden':home_garden,
        'electronics':electronics,
        'fashion':fashion,
        'furniture':furniture,
        'healthy_beauty':healthy_beauty,
        'gift_ideas':gift_ideas,
        'cooking':cooking,
        'smart_phones':smart_phones,
        'cameras_photo':cameras_photo,
        'accessories':accessories,
        'toy_games':toy_games,
    }

    return render(request,"core/about.html",context)

def contact_us(request):
    cart = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    
    sub_sub_category = SubSubCategory.objects.all()
    sub_category = SubCategory.objects.all()
    category = Category.objects.all()

    home_garden = []
    electronics = []
    fashion = []
    furniture = []
    healthy_beauty = []
    gift_ideas = []
    toy_games = []
    cooking = []
    smart_phones = []
    cameras_photo = []
    accessories = []


    for i in sub_category:
        if i.category.filtername == "home_&_garden":
            home_garden.append(i.name)
        elif i.category.filtername == "electronics":
            electronics.append(i.name)
        elif i.category.filtername == "fashion":
            fashion.append(i.name)
        elif i.category.filtername == "furniture":
            furniture.append(i.name)
        elif i.category.filtername == "healthy_&_beauty":
            healthy_beauty.append(i.name)
        elif i.category.filtername == "gift_ideas":
            gift_ideas.append(i.name)
        elif i.category.filtername == "toy_&_games":
            toy_games.append(i.name)
        elif i.category.filtername == "cooking":
            cooking.append(i.name)
        elif i.category.filtername == "smart_phones":
            smart_phones.append(i.name)
        elif i.category.filtername == "cameras_&_photo":
            cameras_photo.append(i.name)
        elif i.category.filtername == "accessories":
            accessories.append(i.name)

    context = {
        'navbar':'contact_us',
        'cart':cart,
        'sub_sub_category':sub_sub_category,
        'sub_category':sub_category,
        'home_garden':home_garden,
        'electronics':electronics,
        'fashion':fashion,
        'furniture':furniture,
        'healthy_beauty':healthy_beauty,
        'gift_ideas':gift_ideas,
        'cooking':cooking,
        'smart_phones':smart_phones,
        'cameras_photo':cameras_photo,
        'accessories':accessories,
        'toy_games':toy_games,

    }
    return render(request,"core/contact_us.html",context)

def faq(request):
    cart = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)

    sub_sub_category = SubSubCategory.objects.all()
    sub_category = SubCategory.objects.all()
    category = Category.objects.all()

    home_garden = []
    electronics = []
    fashion = []
    furniture = []
    healthy_beauty = []
    gift_ideas = []
    toy_games = []
    cooking = []
    smart_phones = []
    cameras_photo = []
    accessories = []


    for i in sub_category:
        if i.category.filtername == "home_&_garden":
            home_garden.append(i.name)
        elif i.category.filtername == "electronics":
            electronics.append(i.name)
        elif i.category.filtername == "fashion":
            fashion.append(i.name)
        elif i.category.filtername == "furniture":
            furniture.append(i.name)
        elif i.category.filtername == "healthy_&_beauty":
            healthy_beauty.append(i.name)
        elif i.category.filtername == "gift_ideas":
            gift_ideas.append(i.name)
        elif i.category.filtername == "toy_&_games":
            toy_games.append(i.name)
        elif i.category.filtername == "cooking":
            cooking.append(i.name)
        elif i.category.filtername == "smart_phones":
            smart_phones.append(i.name)
        elif i.category.filtername == "cameras_&_photo":
            cameras_photo.append(i.name)
        elif i.category.filtername == "accessories":
            accessories.append(i.name)

    context = {
        'navbar':'faq',
        'cart':cart,
        'sub_sub_category':sub_sub_category,
        'sub_category':sub_category,
        'home_garden':home_garden,
        'electronics':electronics,
        'fashion':fashion,
        'furniture':furniture,
        'healthy_beauty':healthy_beauty,
        'gift_ideas':gift_ideas,
        'cooking':cooking,
        'smart_phones':smart_phones,
        'cameras_photo':cameras_photo,
        'accessories':accessories,
        'toy_games':toy_games,
    }
    return render(request,"core/faq.html",context)

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

    sub_sub_category = SubSubCategory.objects.all()
    sub_category = SubCategory.objects.all()
    category = Category.objects.all()

    home_garden = []
    electronics = []
    fashion = []
    furniture = []
    healthy_beauty = []
    gift_ideas = []
    toy_games = []
    cooking = []
    smart_phones = []
    cameras_photo = []
    accessories = []


    for i in sub_category:
        if i.category.filtername == "home_&_garden":
            home_garden.append(i.name)
        elif i.category.filtername == "electronics":
            electronics.append(i.name)
        elif i.category.filtername == "fashion":
            fashion.append(i.name)
        elif i.category.filtername == "furniture":
            furniture.append(i.name)
        elif i.category.filtername == "healthy_&_beauty":
            healthy_beauty.append(i.name)
        elif i.category.filtername == "gift_ideas":
            gift_ideas.append(i.name)
        elif i.category.filtername == "toy_&_games":
            toy_games.append(i.name)
        elif i.category.filtername == "cooking":
            cooking.append(i.name)
        elif i.category.filtername == "smart_phones":
            smart_phones.append(i.name)
        elif i.category.filtername == "cameras_&_photo":
            cameras_photo.append(i.name)
        elif i.category.filtername == "accessories":
            accessories.append(i.name)

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

    sub_sub_category = SubSubCategory.objects.all()

    sub_category = SubCategory.objects.all()
    category = Category.objects.all()

    home_garden = []
    electronics = []
    fashion = []
    furniture = []
    healthy_beauty = []
    gift_ideas = []
    toy_games = []
    cooking = []
    smart_phones = []
    cameras_photo = []
    accessories = []


    for i in sub_category:
        if i.category.filtername == "home_&_garden":
            home_garden.append(i.name)
        elif i.category.filtername == "electronics":
            electronics.append(i.name)
        elif i.category.filtername == "fashion":
            fashion.append(i.name)
        elif i.category.filtername == "furniture":
            furniture.append(i.name)
        elif i.category.filtername == "healthy_&_beauty":
            healthy_beauty.append(i.name)
        elif i.category.filtername == "gift_ideas":
            gift_ideas.append(i.name)
        elif i.category.filtername == "toy_&_games":
            toy_games.append(i.name)
        elif i.category.filtername == "cooking":
            cooking.append(i.name)
        elif i.category.filtername == "smart_phones":
            smart_phones.append(i.name)
        elif i.category.filtername == "cameras_&_photo":
            cameras_photo.append(i.name)
        elif i.category.filtername == "accessories":
            accessories.append(i.name)

        return render(request,"core/checkout.html",locals())
    else:
        return redirect("login")


def orderpage(request,pk):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        order = Order.objects.get(user=request.user,id=pk)
        orderitems = OrderItems.objects.filter(user=request.user,order=order)

        sub_sub_category = SubSubCategory.objects.all()
    sub_category = SubCategory.objects.all()
    category = Category.objects.all()

    home_garden = []
    electronics = []
    fashion = []
    furniture = []
    healthy_beauty = []
    gift_ideas = []
    toy_games = []
    cooking = []
    smart_phones = []
    cameras_photo = []
    accessories = []


    for i in sub_category:
        if i.category.filtername == "home_&_garden":
            home_garden.append(i.name)
        elif i.category.filtername == "electronics":
            electronics.append(i.name)
        elif i.category.filtername == "fashion":
            fashion.append(i.name)
        elif i.category.filtername == "furniture":
            furniture.append(i.name)
        elif i.category.filtername == "healthy_&_beauty":
            healthy_beauty.append(i.name)
        elif i.category.filtername == "gift_ideas":
            gift_ideas.append(i.name)
        elif i.category.filtername == "toy_&_games":
            toy_games.append(i.name)
        elif i.category.filtername == "cooking":
            cooking.append(i.name)
        elif i.category.filtername == "smart_phones":
            smart_phones.append(i.name)
        elif i.category.filtername == "cameras_&_photo":
            cameras_photo.append(i.name)
        elif i.category.filtername == "accessories":
            accessories.append(i.name)

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