from django.contrib import admin

from thrift_marketplace.products.models import Category, Product, Photos


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    ordering = ('pk',)
    list_filter = ('name',)
    filter = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category', 'product_name', 'price', 'user')
    list_filter = ('category_id', )
    ordering = ('pk', 'category')
    search_fields = ("product_name__icontains",)
    filter = ('product_name', 'category')



@admin.register(Photos)
class ProductPhotosAdmin(admin.ModelAdmin):
    list_display = ('pk', 'photo_picture', 'category', 'product', 'product_pk', 'username')
    ordering = ('pk',)

    @staticmethod
    def category(current_photo_obj):
        current_category = current_photo_obj.product.category
        return current_category

    @staticmethod
    def product_pk(current_photo_obj):
        current_product = current_photo_obj.product.pk
        return current_product

    @staticmethod
    def username(current_photo_obj):
        current_product = current_photo_obj.product.user.username
        return current_product

