from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from home.models import User, Booking, Mentor, Woman


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('id', 'username', 'email', 'type', 'is_staff', 'is_active',)
    list_filter = ('type', 'is_staff', 'is_active',)
    fieldsets = (
        ('Type', {'fields': ('type',)}),
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': (
            'is_active', 'is_staff', 'is_superuser',
            'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2',
                'type', 'is_staff', 'is_active')}),)
    search_fields = ('username', 'email',)
    ordering = ('id',)

class WomanAdmin(UserAdmin):
    model = Woman
    list_display = ('id', 'username', 'email', 'type', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    search_fields = ('username', 'email',)
    ordering = ('id',)


class MentorAdmin(UserAdmin):
    model = Mentor
    list_display = ('id', 'username', 'email', 'type', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    search_fields = ('username', 'email',)
    ordering = ('id',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Woman, WomanAdmin)
admin.site.register(Mentor, MentorAdmin)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'user', 'date', 'time')
