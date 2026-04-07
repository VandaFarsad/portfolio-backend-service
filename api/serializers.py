from rest_framework import serializers

from api.models import Experience, StackIcon, TechnologyChoices


class StackIconSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="icon", read_only=True)
    name = serializers.CharField(source="icon_text", read_only=True)
    label = serializers.CharField(source="get_icon_display", read_only=True)

    class Meta:
        model = StackIcon
        fields = ("id", "name", "label", "order")


class ExperienceSerializer(serializers.ModelSerializer):
    date_range = serializers.CharField(read_only=True)
    is_current = serializers.BooleanField(read_only=True)
    stack = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = (
            "id",
            "category",
            "start_date",
            "end_date",
            "date_range",
            "is_current",
            "organization",
            "position",
            "stack",
        )

    def get_stack(self, obj):
        """Return full technology labels instead of just the values"""
        return [dict(TechnologyChoices.choices).get(tech, tech) for tech in obj.stack]
