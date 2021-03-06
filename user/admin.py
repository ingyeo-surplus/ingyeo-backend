from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('user_id', 'username', 'is_staff', 'is_active',)
    list_filter = ('user_id', 'username', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('user_id', 'username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('user_id', 'username',)
    ordering = ('user_id', 'username',)


admin.site.register(CustomUser, CustomUserAdmin)
