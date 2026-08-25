from django.urls import path, include

urlpatterns = [
    path("image/", include("gallery.urls.image_urls")),
]
