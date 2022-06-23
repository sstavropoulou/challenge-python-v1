from django.urls import path

from . import views

app_name = "dinosaurs"

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.DinosaurListAPIView.as_view(), name="dinosaur-list"),
    path("<int:pk>/", views.DinosaurAPIView.as_view(), name="dinosaur-detail"),
    path("create/", views.DinosaurCreateAPIView.as_view(), name="dinosaur-create"),
    path("search/", views.SearchDinosaurAPIView.as_view(), name="dinosaur-search"),
    path("<int:pk>/like/", views.DinosaurLikeAPIView.as_view(), name="dinosaur-like"),
]
