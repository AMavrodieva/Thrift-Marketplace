from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from thrift_marketplace.common.forms import SearchProductsForm, SearchCategoryForm
from thrift_marketplace.products.models import Product

UserModel = get_user_model()


def index(request):
    search_form = SearchProductsForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['product_name']

    search_category_form = SearchCategoryForm(request.GET)
    search_category_pattern = None
    if search_category_form.is_valid():
        search_category_pattern = search_category_form.cleaned_data['name']

    products = Product.objects.all().order_by('-date_of_publication')

    if search_pattern:
        products = products.filter(product_name__icontains=search_pattern.lower())
    if search_category_pattern:
        products = products.filter(category__name=search_category_pattern)

    products_paginate_by = 6
    paginator = Paginator(products, products_paginate_by)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'products': products,
        'search_form': search_form,
        'search_category_form': search_category_form,
        'page_obj': page_obj,
    }

    return render(request, 'common/home-page.html', context)
