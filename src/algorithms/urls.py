from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'algorithms', views.AlgorithmViewSet, basename="algorithm_view_set")

app_name = "algorithms"
urlpatterns = [
    path("", views.index, name="index"),
    path("algorithms/<int:algorithm_id>/", views.get_algo_details, name="get_algo_details"),
    path("algorithms/upload/", views.upload_algorithm, name="upload_algorithm"),
    path("", include(router.urls)),
]