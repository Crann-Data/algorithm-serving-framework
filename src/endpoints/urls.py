from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.EndpointViewSet, basename="endpoint_view_set")

app_name = "endpoints"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("create_endpoint/", views.CreateEndpoint.as_view(), name="create_endpoint"),
    path("api/", include(router.urls)),
]