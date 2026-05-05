from django.contrib import admin
from .models import BetaSignup


@admin.register(BetaSignup)
class BetaSignupAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'name', 'contact', 'business_type', 'created_at')
    search_fields = ('name', 'business_name', 'contact')
    list_filter = ('business_type', 'created_at')
