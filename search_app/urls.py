from django.urls import path
from .views import search_result
app_name='search_app'
urlpatterns=[
    path('',search_result,name="searchResult")
]