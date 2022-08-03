from django.urls import path
from products.views import list_products, create_product

urlpatterns = [
    path('create-product/', create_product, name='create_product'),
    path('list-products/', list_products, name = 'list_products'),
]