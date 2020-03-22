from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('adduser',views.adduser,name='user'),
    path('new', views.newbook, name='newbook'),
    path('cart', views.cart, name='cart'),
    path('<book_id>/edit',views.editbook,name='editbook'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logout_user,name='logout'),
]
