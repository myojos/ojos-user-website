from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import OjosUserChangeForm, OjosUserCreationForm
from .models import OjosUser


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = OjosUserChangeForm
    add_form = OjosUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'country', 'phone_number', 'is_active', 'is_admin')
    list_filter = ('is_admin', 'country', 'date_joined')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Billing', {'fields': ('date_joined',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'country', 'phone_number', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('date_joined',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(OjosUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
