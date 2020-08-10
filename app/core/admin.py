from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# recommended way to display message to user
from django.utils.translation import gettext as _
from core import models

# this allow us to create custom user admin


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    # this creates the sections in our admin page
    fieldsets = (
        (None, {'fields': ('email', "password",)}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser',)
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        })
    )


admin.site.register(models.User, UserAdmin)
