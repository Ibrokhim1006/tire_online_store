from django.urls import path
from online_shop.views import *

urlpatterns = [
    path('',index,name='index'),
]