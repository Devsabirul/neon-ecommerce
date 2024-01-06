from django.contrib import admin
from .models import *


admin.site.register([Category,SubCategory,Products,PopularDepartMents])
admin.site.register(Cart)
admin.site.register([Customer,Order,OrderItems])
