from rest_framework import serializers

from api.models import Experience, StackIcon


class StackIconSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StackIcon
        fields = ("icon_set_prefix", "icon_name", "text", "icon")


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experience
        fields = ("type", "date", "title", "subtitle", "tags")
