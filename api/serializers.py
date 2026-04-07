from rest_framework import serializers

from api.models import Experience, StackIcon


class StackIconSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField(source="icon", read_only=True)
    name = serializers.CharField(source="icon_text", read_only=True)
    order = serializers.IntegerField(source="order", read_only=True)

    class Meta:
        model = StackIcon
        fields = ("id", "name", "order")


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Experience
        fields = ("id", "type", "date", "title", "subtitle", "tags")
