# core/admin.py
from django.contrib import admin
from .models import Contact, SignUp  # Make sure this import is correct

# Register Contact model
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

# Register SignUp model
@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'truck_type', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('truck_type', 'created_at')
    readonly_fields = ('created_at',)