from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super().save(*args, **kwargs)


class Products(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sku = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    review = models.PositiveIntegerField(null=True,blank=True,default=0)
    sort_description = RichTextField()
    slug = AutoSlugField(populate_from="name", null=True, unique=True)
    description = RichTextField()
    image = models.ImageField(upload_to="Product Image")


    def __str__(self):
        return str(self.name)

class PopularDepartMents(models.Model):
    Department = (
        ('NEWARRIVALS', 'NEWARRIVALS'),
        ('BESTSELLER', 'BESTSELLER'),
        ('MOSTPOPULAR', 'MOSTPOPULAR'),
        ('FEATURED', 'FEATURED'),
    )

    department = models.CharField(choices=Department, max_length=100)
    products  = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.department
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products,  on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def line_total(self):
        return self.quantity * self.product.price


# class Customer(models.Model):
#     country = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     company_name = models.CharField(max_length=100,null=True,blank=True)
#     Address = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zipcode = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)

#     def __str__(self):
#         return self.first_name
    

# class Shipping(models.Model):
#     country = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     company_name = models.CharField(max_length=100,null=True,blank=True)
#     Address = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zipcode = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)

#     def __str__(self):
#         return self.first_name
    

# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE)
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateField( auto_now=False, auto_now_add=True)
#     status = models.CharField(max_length=100,default="panding")
#     pymentSystem = models.CharField(max_length=100,default="cashondelivery")
#     ordernote = models.TextField()

#     def __str__(self):
#         return self.status
