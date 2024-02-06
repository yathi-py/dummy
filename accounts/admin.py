from django.contrib import admin

from accounts.models import User


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_active')

    fieldsets = (
        ('General Information',{
            'fields': ('email','username', 'is_active', 'is_superuser'),
        }),
    )


admin.site.register(User, UserAdmin)
