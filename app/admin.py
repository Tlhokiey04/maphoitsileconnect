from django.contrib import admin
from .models import Issue, Profile

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display   = ['pk', 'user', 'category', 'location', 'status', 'created_at']
    list_filter    = ['status', 'category']
    search_fields  = ['user__username', 'location', 'description']
    list_editable  = ['status']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display  = ['user', 'phone_number', 'suburb']
    search_fields = ['user__username', 'suburb']