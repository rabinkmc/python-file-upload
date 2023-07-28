from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet
from .models import UploadedFile
from .serializers import UploadedFileSerializer


class UploadedFileViewSet(ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    parser_classes = [MultiPartParser]

    def perform_create(self, serializer):
        serializer.save(file=self.request.data["file"])
