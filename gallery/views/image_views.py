import mimetypes

from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404

from ..models import Image


def image_file(request, pk):
    image = get_object_or_404(Image, pk=pk)

    if not image.is_public and not request.user.is_authenticated:
        raise Http404

    if not image.image:
        raise Http404

    content_type, _ = mimetypes.guess_type(image.image.name)

    return FileResponse(
        image.image.open("rb"),
        content_type=content_type or "application/octet-stream",
    )
