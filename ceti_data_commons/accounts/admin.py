from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'g_id')
    list_display_links = ('user', 'g_id')
    search_fields = ('user', 'g_id')
    list_per_page = 25


admin.site.register(UserProfile, UserProfileAdmin)
