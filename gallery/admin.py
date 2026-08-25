from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    autocomplete_fields = ("uploaded_by",)
    date_hierarchy = "created_at"
    list_display = (
        "title",
        "uploaded_by",
        "is_public",
        "created_at",
        "updated_at",
        "image_preview",
    )

    list_filter = (
        "is_public",
        "created_at",
        "uploaded_by",
    )

    search_fields = (
        "title",
        "description",
        "uploaded_by__username",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "image_preview",
    )

    fieldsets = (
        (
            "Image Details",
            {
                "fields": (
                    "title",
                    "description",
                    "image",
                    "image_preview",
                )
            },
        ),
        (
            "Access",
            {
                "fields": (
                    "uploaded_by",
                    "is_public",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    @admin.display(description="Preview")
    def image_preview(self, obj):
        if not obj.image:
            return "No image"

        url = reverse(
            "image:file",
            kwargs={"pk": obj.pk},
        )

        return format_html(
            '<img src="{}" style="max-width: 150px; max-height: 100px; '
            'object-fit: contain; border-radius: 8px;" />',
            url,
        )
