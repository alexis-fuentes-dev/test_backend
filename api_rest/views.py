from django.http.response import JsonResponse
from django.views.defaults import page_not_found
from django.views import View
from .models import Category, Product
import json

# Error personalizado
def mi_error_404(request, exception):
    nombre_template = '404.html'
    return page_not_found(request, template_name=nombre_template)

# Listar categorias y productos de las categorias
class CategoryView(View):
    def get(self, request, id = 0):
        data = {}
        if id > 0:
            # Buscamos los productos de la categoria
            products = list(Product.objects.filter(category=id).values())
            if len(products) > 0:
                data = {'message': 'success', 'products': products}
            else:
                data = {'message': 'Products not found'}
        else:
            categorias = list(Category.objects.values())
            if len(categorias) > 0:
                data = {'message': 'success', 'categories': categorias}
            else:
                data = {'message': 'Categories not found'}

        return JsonResponse(data)

class ProductsView(View):
    def get(self, request, id = 0):
        data = {}
        if id == 0:
            data = {'message': 'Product not  found'}
        else:
            product = list(Product.objects.filter(id=id).values)
            if len(product) > 0:
                data = {'message': 'success', 'product': product[0]}
            else:
                data = {'message': 'Product not found'}
        
        return JsonResponse(data)
