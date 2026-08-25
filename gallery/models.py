from django.conf import settings
from django.db import models
from django.core.files.storage import FileSystemStorage

private_storage = FileSystemStorage(
    location=settings.PRIVATE_MEDIA_ROOT,
)


class Image(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="gallery/%Y/%m/",
        storage=private_storage,
    )

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="gallery_images",
    )

    is_public = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
