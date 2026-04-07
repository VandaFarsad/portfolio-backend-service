from django.contrib import admin

from api.models import Experience, StackIcon


@admin.register(StackIcon)
class StackIconAdmin(admin.ModelAdmin):
    list_display = ("order", "icon", "icon_text", "get_icon_label")
    list_display_links = ("icon",)
    list_editable = ("order", "icon_text")
    search_fields = ("icon", "icon_text")
    list_filter = ("icon",)
    ordering = ("order",)

    @admin.display(description="Label")
    def get_icon_label(self, obj):
        return obj.get_icon_display()


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("type", "date", "title", "subtitle", "display_tags")
    list_display_links = ("title",)
    search_fields = ("type", "title", "subtitle")
    list_filter = ("type", "date")
    ordering = ("-date",)

    @admin.display(description="Tags")
    def display_tags(self, obj):
        return ", ".join(obj.tags) if obj.tags else "-"
