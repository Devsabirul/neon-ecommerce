from django.urls import path 
from .views import *


urlpatterns = [
    path('login',login_,name="login"),
    path('registration',registration,name="registration"),
    path('my_account',my_account,name="my_account"),
    path('signout', signout, name="signout"),
]
