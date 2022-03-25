from django.middleware.csrf import get_token
from rest_framework import viewsets, status
from django.http.response import StreamingHttpResponse
from django.contrib.auth.models import User
from sources.models import Source
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from sources.api.serializers import (
    SourceWithChildrenSerializer,
    SourceSerializer,
    SourceCreateDirSerializer,
    SourceDownloadSerializer
)
from utils.permissions import IsSourceOwner
from rest_framework.response import Response
from utils.modelshelpers.enums import FileType
from sources.SourceServer import SourceServer


class SourceViewSet(viewsets.GenericViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

    def get_permissions(self):
        return IsAuthenticated(), IsSourceOwner()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if int(instance.type) == FileType.DIR:
            return Response(SourceWithChildrenSerializer(instance).data, status=status.HTTP_200_OK)
        else:
            return Response(SourceSerializer(instance).data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True, permission_classes=(IsAuthenticated, IsSourceOwner))
    def upload(self, request, pk):
        parent_dir = Source.objects.filter(id=int(pk))
        if not parent_dir:
            return Response({
                'errors': 'The dir is not exists'
            }, status=status.HTTP_400_BAD_REQUEST)
        file = request.FILES.get('file', None)
        if not file:
            return Response({
                'errors': 'file is None'
            }, status=status.HTTP_400_BAD_REQUEST)
        filename = file.name
        source = Source.objects.create(
            parent_dir_id=int(pk),
            name=filename,
            owner=request.user,
            type=FileType.FILE
        )
        if not SourceServer.create_sources(source, file.read()):
            return Response({
                'error': "Upload error, please check input"
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'success': 'ok'
        }, status=status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=True, permission_classes=(IsAuthenticated, IsSourceOwner))
    def create_dir(self, request, pk):
        serializer = SourceCreateDirSerializer(data=request.data, context={'request': request, 'pk': pk})
        if not serializer.is_valid():
            return Response({
                'message': 'please check input',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        source = serializer.save()
        return Response({
            'success': 'ok',
            'dir': SourceSerializer(source).data,
        }, status=status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=True, permission_classes=(IsAuthenticated, IsSourceOwner))
    def download(self, request, pk):
        serializer = SourceDownloadSerializer(data=request.data, context={'pk': pk})
        if not serializer.is_valid():
            return Response({
                'message': 'download error',
                'errors': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
        path = SourceServer.make_full_path(serializer.validated_data['path'])
        f = open(path, 'rb')
        response = StreamingHttpResponse(f)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = f'attachment;filename={request.data["name"]}'
        return response
