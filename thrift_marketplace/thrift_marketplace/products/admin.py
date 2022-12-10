from django.contrib import admin

from thrift_marketplace.products.models import Category, Product, Photos


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('pk',)
    list_filter = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'pk', 'product_name', 'price')
    list_filter = ('category_id', )
    ordering = ('category', 'pk')


@admin.register(Photos)
class ProductPhotosAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'photo_picture', 'category')
    ordering = ('pk',)

    @staticmethod
    def category(current_photo_obj):
        current_category = current_photo_obj.product.category
        return current_category
