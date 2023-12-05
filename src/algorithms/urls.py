from django.urls import path

from . import views

app_name = "algorithms"
urlpatterns = [
    path("", views.index, name="index"),
    path("algorithms/<int:algorithm_id>/", views.get_algo_details, name="get_algo_details"),
    path("algorithms/upload/", views.upload_algorithm, name="upload_algorithm"),
]