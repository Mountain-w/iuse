from rest_framework import viewsets, status
from rest_framework.response import Response
from sources.models import Source
from utils.modelshelpers.enums import FileType, DeleteStatus
from utils.permissions import IsSourceOwner
from rest_framework.permissions import IsAuthenticated
from .serializers import ContentSerializer


class EditorViewSet(viewsets.GenericViewSet):
    queryset = Source.objects.filter(on_delete=DeleteStatus.exists, type=FileType.FILE).all()

    def get_permissions(self, *args, **kwargs):
        return IsAuthenticated(), IsSourceOwner()

    def retrieve(self, request, pk):
        instance = self.get_object()
        content = instance.content
        return Response({
            'content': ContentSerializer(content).data
        }, status=status.HTTP_200_OK)
