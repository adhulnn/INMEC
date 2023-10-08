from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path('',views.allCat,name="allCat"),
    path('<slug:c_slug>/',views.allCat,name="products_by_category"),

]