from django import forms
from django.contrib import admin

from api.models import Experience, StackIcon, TechnologyChoices


class ExperienceAdminForm(forms.ModelForm):
    stack = forms.MultipleChoiceField(
        choices=TechnologyChoices.choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Verwendete Technologien",
    )

    class Meta:
        model = Experience
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.stack:
            self.initial["stack"] = self.instance.stack


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
    form = ExperienceAdminForm
    list_display = ("category", "organization", "position", "get_date_range", "display_stack")
    list_display_links = ("organization",)
    search_fields = ("organization", "position")
    list_filter = ("category", "start_date", "end_date")
    ordering = ("-start_date",)
    fieldsets = (
        ("Kategorie", {"fields": ("category",)}),
        ("Zeitraum", {"fields": ("start_date", "end_date")}),
        ("Details", {"fields": ("organization", "position")}),
        ("Technologien", {"fields": ("stack",), "classes": ("collapse",)}),
    )

    @admin.display(description="Zeitraum", ordering="start_date")
    def get_date_range(self, obj):
        return obj.date_range

    @admin.display(description="Stack")
    def display_stack(self, obj):
        return ", ".join(obj.stack) if obj.stack else "-"
