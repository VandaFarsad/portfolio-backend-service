from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models import Experience, StackIcon
from api.serializers import ExperienceSerializer, StackIconSerializer


class StackIconViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = StackIcon.objects.all()
    serializer_class = StackIconSerializer
    http_method_names = ["get"]


class ExperienceViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    http_method_names = ["get"]
