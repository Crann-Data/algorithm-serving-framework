from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.DeploymentNodeViewSet, basename="deploymentNodes_view_set")

app_name = "deploymentNodes"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("api/", include(router.urls)),
]