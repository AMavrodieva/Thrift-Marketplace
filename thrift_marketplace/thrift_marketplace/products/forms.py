from django import forms

from thrift_marketplace.common.models import ProductComment, ProductRequest, ProductRating
from thrift_marketplace.products.models import Product, Photos


class BaseProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('date_of_publication', 'user')
        widgets = {
            'product_name': forms.TextInput(attrs={'placeholder': 'Product name'},),
            'product_picture': forms.FileInput(attrs={'placeholder': 'Product picture'},),
            'description': forms.Textarea(attrs={'placeholder': 'Add description...'},),
            'location': forms.TextInput(attrs={'placeholder': 'City'}, ),
            'price': forms.TextInput(attrs={'placeholder': "0.00 lv."},),
        }


class CreateProductForm(BaseProductForm):
    pass


class EditProductForm(BaseProductForm):
    pass


class DeleteProductForm(BaseProductForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            Photos.objects.filter(product_id=self.instance.id).delete()
            ProductComment.objects.filter(product_id=self.instance.id).delete()
            ProductRequest.objects.filter(product_id=self.instance.id).delete()
            ProductRating.objects.filter(product_id=self.instance.id).delete()
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False


class ProductPhotoAddForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ('photo_picture',)

