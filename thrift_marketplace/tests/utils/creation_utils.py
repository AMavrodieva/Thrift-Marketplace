from thrift_marketplace.common.models import ProductRequest, ProductComment, ProductRating
from thrift_marketplace.products.models import Category, Product, Photos


def create_category():
    category = Category(name='Phones & Tablets')
    category.save()
    return category


def create_product(user):
    category = create_category()
    product = Product(
        user=user,
        category=category,
        product_name='SomeProduct',
        price='50',
    )
    product.save()
    return product


def create_request(user, product):
    product_request = ProductRequest(
        text="Some text",
        request_email="test@gmail.com",
        product=product,
        user=user
    )
    product_request.save()
    return product_request


def create_comment(user, product):
    comment = ProductComment(
        text="Some text",
        product=product,
        user=user
    )
    comment.save()
    return comment


def create_rating(user, product):
    rating = ProductRating(
        review_rating="1",
        user=user,
        product=product,
    )
    rating.save()
    return int(rating.review_rating)


def create_photo(user, product):
    product_photo = Photos(
        user=user,
        product=product,
        photo_picture='image/upload/v1670704901/pcratnrc4wj8jp.jpg'
    )
    product_photo.save()
    return product_photo
