from django.contrib import admin
from django.contrib.auth import get_user_model

from thrift_marketplace.accounts.forms import AppChangeUserForm, AppCreateUserForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff',)
    ordering = ('email',)
    search_fields = ("first_name__startswith",)
    add_form = AppCreateUserForm

    fieldsets = (
        (
            None,
            {'fields': ('username', 'email', 'password'), }),
        (
            'Personal info',
            {'fields': ('first_name', 'last_name'), },),
        (
            'Permissions',
            {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',), },),
        (
            'Important dates',
            {'fields': ('last_login', 'date_joined',), },),
    )

    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)
