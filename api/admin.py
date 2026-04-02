from django.contrib import admin

from api.models import Experience, StackIcon


@admin.register(StackIcon)
class StackIconAdmin(admin.ModelAdmin):
    list_display = ("position", "icon_set_prefix", "icon_name", "text", "icon")
    search_fields = ("icon_set_prefix", "icon_name", "text", "icon")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("type", "date", "title", "subtitle", "tags")
    search_fields = ("type", "date", "title", "subtitle", "tags")
    list_filter = ("type",)
