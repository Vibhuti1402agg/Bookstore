from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('form.html',views.register, name='add'),
    path('adduser',views.adduser,name='user'),
    path('new', views.newbook, name='newbook'),
    path('cart', views.cart, name='cart'),
]
