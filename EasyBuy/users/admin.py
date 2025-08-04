from django.contrib import admin
from .models import User, UserProfile, Role, UserRole

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('email',)
    ordering = ('-date_joined',)
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Important dates', {'fields': ('date_joined',)}),
    )

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number')
    search_fields = ('user__email', 'first_name', 'last_name')
    ordering = ('user__email',)

admin.site.register(Role)
admin.site.register(UserRole)