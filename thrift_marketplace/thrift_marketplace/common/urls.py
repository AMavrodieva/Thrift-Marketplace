from django.urls import path

from thrift_marketplace.common.views import index


urlpatterns = (
    path("", index, name='index'),
)
