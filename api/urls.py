from django.urls import include, path
from rest_framework import routers

from api.views import ExperienceViewSet, StackIconViewSet

router = routers.DefaultRouter()
router.register(r"experiences", ExperienceViewSet)
router.register(r"stackicons", StackIconViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
