from rest_framework import viewsets

from api.models import Experience, StackIcon
from api.serializers import ExperienceSerializer, StackIconSerializer


class StackIconViewSet(viewsets.ModelViewSet):
    queryset = StackIcon.objects.all()
    serializer_class = StackIconSerializer
    http_method_names = ["get"]


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    http_method_names = ["get"]
