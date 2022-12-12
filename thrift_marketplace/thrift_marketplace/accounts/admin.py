from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from thrift_marketplace.accounts.forms import AppCreateUserForm, AppChangeUserForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'group')
    ordering = ('email',)
    search_fields = ("username__startswith",)
    filter = ('username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff')
    form = AppChangeUserForm
    add_form = AppCreateUserForm

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)

    group.short_description = 'Groups'

    fieldsets = (
        (
            None,
            {'fields': ('username', 'email', ), },),
        (
            'Personal info',
            {'fields': ('first_name', 'last_name', 'phone_number', 'profile_picture'), },),
        (
            'Permissions',
            {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',), },),
        (
            'Important dates',
            {'fields': ('last_login', 'date_joined',), },),
    )

    add_fieldsets = (
        (
            None,
            {"fields": ('username', 'email', 'password1', 'password2'), },),
        (
            'Personal info',
            {'fields': ('first_name', 'last_name', 'phone_number', 'profile_picture'), },),
        (
            'Permissions',
            {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',), },),
        (
            'Important dates',
            {'fields': ('last_login', 'date_joined',), },),
    )

