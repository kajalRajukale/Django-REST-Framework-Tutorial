from django.contrib import admin
from .models import Snippet

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'language', 'style', 'created')
    list_filter = ('language', 'style', 'owner', 'created')
    search_fields = ('title', 'code', 'owner__username')
    ordering = ('-created',)
    raw_id_fields = ('owner',)
    readonly_fields = ('highlighted',)
