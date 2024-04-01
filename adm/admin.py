from django.contrib import admin

from .models import Note, Comment


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    list_display_links = ('id', 'name', 'date')

admin.site.register(Comment)