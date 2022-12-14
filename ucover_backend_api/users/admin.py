from django.contrib import admin
from .models import users

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','first_name' ,'last_name' ,'is_coverer', 'is_staff', 'is_active',)
    list_filter = ('is_coverer', 'is_staff', 'is_active','created_at','updated_at')

admin.site.register(users.User, CustomUserAdmin)

