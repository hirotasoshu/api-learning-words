import admin_thumbnails
from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Category, Level, Word, Theme


@admin.register(Category)
@admin_thumbnails.thumbnail('icon')
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Theme)
@admin_thumbnails.thumbnail('photo')
class ThemeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Level)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    readonly_fields = ['sound_preview']


admin.site.unregister(Group)
admin.site.unregister(User)
