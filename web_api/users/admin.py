from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'middle_name', 'last_name', 'client']
    list_filter = ('client',)
    fieldsets = UserAdmin.fieldsets + (('Доп. реквизиты', {'fields': ('client', 'middle_name',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (('Доп. реквизиты', {'fields': ('client',)}),)
    search_fields = ('client',)
    ordering = ('client',)

admin.site.register(CustomUser, CustomUserAdmin)
