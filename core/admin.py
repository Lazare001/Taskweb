from django.contrib import admin
from .models import BetaSignup, Post


@admin.register(BetaSignup)
class BetaSignupAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'name', 'contact', 'business_type', 'created_at')
    search_fields = ('name', 'business_name', 'contact')
    list_filter = ('business_type', 'created_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'image')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at',)
