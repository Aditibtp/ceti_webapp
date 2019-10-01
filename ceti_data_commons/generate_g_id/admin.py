# Register your models here.
from django.contrib import admin

from .models import Storage

class StorageAdmin(admin.ModelAdmin):
  list_display = ('storage_id', 'created_at', 'user_id')
  list_display_links = ('storage_id', 'user_id')
  search_fields = ('created_at',)
  list_per_page = 25

admin.site.register(Storage, StorageAdmin)