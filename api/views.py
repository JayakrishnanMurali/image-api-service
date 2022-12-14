from rest_framework import generics
from api.custom_renderers import JPEGRenderer, PNGRenderer
from rest_framework.response import Response
from images.models import Image


class ImageAPIView(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer]

    def get(self, request, *args, **kwargs):
        queryset = Image.objects.get(id=self.kwargs['id']).image
        data = queryset
        return Response(data, content_type='image/jpeg')
