from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'contact', 'active', 'staff')  # Change is_active to active
    list_filter = ('staff', 'active')  # Change is_active to active
    search_fields = ('email', 'username', 'contact')
    ordering = ('email',)
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('username', 'email', 'contact', 'password', 'active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'contact', 'password1', 'password2', 'staff', 'active')}
         ),
    )

    def save_model(self, request, obj, form, change):
        if not change:  # If this is a new user
            obj.set_password(form.cleaned_data['password1'])
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)
