from django.urls import path, include
from thrift_marketplace.products.views import add_product, details_product, edit_product, delete_product, product_photos

urlpatterns = (
    path("add/", add_product, name='add product'),
    path("<int:pk>/", include([
        path("", details_product, name='details product'),
        path("edit/", edit_product, name='edit product'),
        path("delete/", delete_product, name='delete product'),
        path('addphoto/', product_photos, name='product photo'),
    ])),
)

