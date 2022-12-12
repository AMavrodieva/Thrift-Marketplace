from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from thrift_marketplace.common.models import ProductComment, ProductRequest, ProductRating
from thrift_marketplace.products.models import Product, Photos

UserModel = get_user_model()


class AppCreateUserForm(auth_forms.UserCreationForm):
    username = auth_forms.UsernameField(widget=forms.TextInput(attrs={'placeholder': 'Username'},),)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'},),)
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'},),
        label="Password")
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'},),
        label="Repeat password",
    )

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')


class AppLoginForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(widget=forms.TextInput(attrs={'placeholder': 'Username'},),)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}, ),)


class AppChangeUserForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}, ), required=False, )
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}, ), required=False,)
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your phone'}, ), required=False, )

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'phone_number', 'profile_picture')
        exclude = ('password',)
        field_classes = {'username': auth_forms.UsernameField}


class AppDeleteUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            Photos.objects.filter(user_id=self.instance.id).delete()
            products = Product.objects.filter(user_id=self.instance.id)
            for product in products:
                product.productcomment_set.all().delete()
                product.productrequest_set.all().delete()
                product.productrating_set.all().delete()
            products.delete()
            self.instance.delete()
        return self.instance

