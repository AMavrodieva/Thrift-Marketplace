from django import forms
from django.contrib.auth import get_user_model

from thrift_marketplace.products.models import Category


UserModel = get_user_model()


class SearchProductsForm(forms.Form):
    product_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search'},),
    )


class SearchCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        labels = {
            'name': 'Category'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_required_fields()

    def __set_required_fields(self):
        for _, field in self.fields.items():
            field.required = False