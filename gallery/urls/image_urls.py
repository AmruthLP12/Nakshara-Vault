from django.urls import path
from gallery.views import image_views

app_name = "image"

urlpatterns = [
    path("<int:pk>/file/", image_views.image_file, name="file"),
]
