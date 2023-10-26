from django.urls import path
from .views import cart_detail,add_cart,decrease_cart_item,cart_remove
app_name='cart'
urlpatterns=[
    path('add/<int:product_id>/',add_cart,name="add_cart"),
    path('decrease/<int:product_id>/', decrease_cart_item, name='decrease_cart_item'),
    path('delete/<int:product_id>/', cart_remove, name='delete_cart_item'), 
    path('',cart_detail,name="cart_detail"),
]