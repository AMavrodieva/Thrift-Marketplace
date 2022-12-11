from django.contrib import admin

from thrift_marketplace.common.models import ProductComment, ProductRequest, ProductRating


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    pass
    list_display = ('pk', 'category', 'product', 'text')
    search_fields = ("product__startswith", )
    ordering = ('pk', )

    @staticmethod
    def category(current_comment_obj):
        current_category = current_comment_obj.product.category
        return current_category


@admin.register(ProductRequest)
class ProductRequestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'product')
    search_fields = ("text__startswith",)
    filter = ('product',)


@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ('review_rating', 'product', 'category', 'pk')
    search_fields = ("product__startswith",)
    ordering = ('-review_rating', 'pk')
    filter = ('review_rating', 'product', 'category', 'pk')
    list_filter = ('review_rating',)

    @staticmethod
    def category(current_rating_obj):
        current_category = current_rating_obj.product.category
        return current_category
