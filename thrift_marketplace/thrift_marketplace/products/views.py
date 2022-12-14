from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from thrift_marketplace.common.forms import ProductCommentForm, ProductRequestForm, ProductRatingForm
from thrift_marketplace.products.forms import CreateProductForm, EditProductForm, ProductPhotoAddForm, \
    DeleteProductForm
from thrift_marketplace.products.models import Product, Photos

UserModel = get_user_model()


@login_required
def add_product(request):
    if request.method == "GET":
        form = CreateProductForm()
    else:
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'products/add_product.html', context,)


def details_product(request, pk):
    product = Product.objects.filter(pk=pk).get()
    product_rating = product.productrating_set.all()
    total_rating = len(product_rating)
    try:
        avg_rating = sum(int(cr.review_rating) for cr in product_rating) / total_rating
    except ZeroDivisionError:
        avg_rating = 0.0

    context = {
        'product': product,
        'is_owner': product.user == request.user,
        'comment_form': ProductCommentForm,
        'request_form': ProductRequestForm,
        'rating_form': ProductRatingForm,
        'avg_rating': avg_rating,
        'product_comments': product.productcomment_set.all(),
        'product_photos': product.photos_set.all(),
    }
    return render(request, 'products/product_details.html', context)


@login_required
def edit_product(request, pk):
    product = Product.objects.filter(pk=pk).get()
    if not request.user == product.user:
        return redirect('details product', pk=product.pk)
    if request.method == "GET":
        form = EditProductForm(instance=product)
    else:
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('details product', pk=product.pk)
    context = {
        'form': form,
        'product': product,
        'is_owner': product.user == request.user,
        'photo_form': ProductPhotoAddForm,

    }

    return render(request, 'products/product_edit.html', context)


@login_required
def delete_product(request, pk):
    product = Product.objects.filter(pk=pk).get()
    if not request.user == product.user:
        return redirect('details product', pk=product.pk)
    if request.method == "GET":
        form = DeleteProductForm(instance=product)
    else:
        form = DeleteProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'product': product,
        'is_owner': product.user == request.user,
    }

    return render(request, 'products/product_delete.html', context)


@login_required
def product_photos(request, pk):
    product = Product.objects.filter(pk=pk).get()
    if not request.user == product.user:
        return redirect('details product', pk=product.pk)

    form = ProductPhotoAddForm(request.POST, request.FILES)
    if form.is_valid():
        photo = form.save(commit=False)
        photo.product = product
        photo.user = request.user
        photo.save()

        return redirect('details product', pk=product.pk)

    context = {
        'form': form,
        'product': product,
        'is_owner': product.user == request.user,
        'photo_form': ProductPhotoAddForm,
    }
    return render(request, 'products/product_edit.html', context)


