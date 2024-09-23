from django.shortcuts import render
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

class ProductsListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products' 

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'  # Esto definirá el nombre del contexto en el template

