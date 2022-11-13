from django.urls import path
from .views import ProductsView, CategoryView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories_list'),
    path('categories/<int:id>', CategoryView.as_view(), name='products_list'),
    path('products/<int:id>', ProductsView.as_view(), name='product_detail')
]
