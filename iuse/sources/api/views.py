
from rest_framework import viewsets, status
from django.http.response import StreamingHttpResponse


from recyclebin.models import Garbage
from sources.models import Source
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from sources.api.serializers import (
    SourceWithChildrenSerializer,
    SourceSerializer,
    SourceCreateDirSerializer,
    SourceDownloadSerializer,
    SourceDeleteSerializer,
    SourceUploadSerializer
)
from utils.permissions import IsSourceOwner
from rest_framework.response import Response
from utils.modelshelpers.enums import FileType, DeleteStatus
from sources.SourceServer import SourceServer


class SourceViewSet(viewsets.GenericViewSet):
    # 过滤掉 on_delete = DeleteStatus.has_delete 的记录
    queryset = Source.objects.filter(on_delete=DeleteStatus.exists).all()
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
        instance = self.get_object()
        if int(instance.type) != FileType.DIR:
            return Response({
                'message': 'you can not upload file to a file'
            }, status=status.HTTP_400_BAD_REQUEST)
        # 获取文件
        file = request.FILES.get('file', None)
        if not file:
            return Response({
                'errors': 'file is None'
            }, status=status.HTTP_400_BAD_REQUEST)
        filename = file.name
        # 检测文件是否存在，是否合法。
        serializer = SourceUploadSerializer(data={'name': filename}, context={'pk': pk})
        if not serializer.is_valid():
            return Response({
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        # 检测通过，创建文件记录
        source = Source.objects.create(
            parent_dir_id=int(pk),
            name=filename,
            owner=request.user,
            type=FileType.FILE
        )
        # 在文件系统中创建文件
        if not SourceServer.create_sources(source, file.read()):
            return Response({
                'error': "Upload error, please check input"
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'success': 'ok'
        }, status=status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=True, permission_classes=(IsAuthenticated, IsSourceOwner))
    def create_dir(self, request, pk):
        self.get_object()
        # 检测文件是否存在，是否合法
        serializer = SourceCreateDirSerializer(data=request.data, context={'request': request, 'pk': pk})
        if not serializer.is_valid():
            return Response({
                'message': 'please check input',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        # 在文件系统中创建文件夹
        source = serializer.save()
        return Response({
            'success': 'ok',
            'dir': SourceSerializer(source).data,
        }, status=status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=True, permission_classes=(IsAuthenticated, IsSourceOwner))
    def download(self, request, pk):
        self.get_object()
        # 检测文件合法性
        serializer = SourceDownloadSerializer(data=request.data, context={'pk': pk})
        if not serializer.is_valid():
            return Response({
                'message': 'download error',
                'errors': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
        # 生成完整路径
        path = SourceServer.make_full_path(serializer.validated_data['path'])
        f = open(path, 'rb')
        response = StreamingHttpResponse(f)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = f'attachment;filename={request.data["name"]}'
        return response

    @action(methods=['POST'], detail=True, permission_classes=(IsAuthenticated, IsSourceOwner))
    def delete(self, request, pk):
        self.get_object()
        # 检测文件合法性
        serializer = SourceDeleteSerializer(data=request.data, context={'pk': pk})
        if not serializer.is_valid():
            return Response({
                'message': 'Delete error',
                'errors': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
        # 假删除，设置文件 on_delete = DeleteStatus.has_delete
        instance = serializer.validated_data['instance']
        instance.on_delete = DeleteStatus.has_deleted
        instance.save()
        # 在回收站中创建一条删除记录
        Garbage.objects.create(
            source=instance,
            owner=instance.owner
        )
        return Response({'success': 'ok'}, status=status.HTTP_200_OK)
