from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.AlgorithmViewSet, basename="algorithm_view_set")

app_name = "algorithms"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("<int:algorithm_id>/", views.AlgoDetails.as_view(), name="get_algo_details"),
    path("download/<int:algorithm_id>/", views.DownloadAlgorithm.as_view(), name="download_algorithm"),
    path("upload/", views.UploadAlgorithm.as_view(), name="upload_algorithm"),
    path("api/", include(router.urls)),
]