from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from thrift_marketplace.common.forms import SearchProductsForm, SearchCategoryForm, ProductCommentForm, \
    ProductRequestForm, ProductRatingForm
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

    products = Product.objects.all().order_by('-pk', '-date_of_publication')

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
        'comment_form': ProductCommentForm,
    }

    return render(request, 'common/home-page.html', context)


@login_required
def product_comment(request, product_id):
    product = Product.objects.filter(pk=product_id).get()

    form = ProductCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.product = product
        comment.user = request.user
        comment.save()

    return redirect('details product', pk=product.pk)


@login_required
def product_request(request, product_id):
    product = Product.objects.filter(pk=product_id).get()

    form = ProductRequestForm(request.POST)

    if form.is_valid():
        query = form.save(commit=False)
        query.product = product
        query.user = request.user
        query.save()
        subject = 'Notification from Thrift Marketplace'
        html_message = render_to_string('common/notification.html', {
            'user': product.user.username,
        })
        email_content = strip_tags(html_message)

        send_mail(
            subject=subject,
            message=email_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=(product.user.email,),
        )

    return redirect('details product', pk=product.pk)


@login_required
def product_rating(request, product_id):
    product = Product.objects.filter(pk=product_id).get()

    form = ProductRatingForm(request.POST)
    if form.is_valid():
        rating = form.save(commit=False)
        rating.product = product
        rating.user = request.user
        rating.save()

    return redirect('details product', pk=product.pk)

