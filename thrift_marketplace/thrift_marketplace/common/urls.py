from django.urls import path

from thrift_marketplace.common.views import index, product_comment, product_request, product_rating

urlpatterns = (
    path("", index, name='index'),
    path('comment/<int:product_id>/', product_comment, name='product comment'),
    path('query/<int:product_id>/', product_request, name='product request'),
    path('rating/<int:product_id>/', product_rating, name='product rating'),
)
