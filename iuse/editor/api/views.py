from rest_framework import viewsets, status
from rest_framework.response import Response
from sources.models import Source
from utils.modelshelpers.enums import FileType, DeleteStatus
from utils.permissions import IsSourceOwner
from rest_framework.permissions import IsAuthenticated
from .serializers import ContentSerializer, FilterSerializer
from rest_framework.decorators import action


class EditorViewSet(viewsets.GenericViewSet):
    queryset = Source.objects.filter(on_delete=DeleteStatus.exists, type=FileType.FILE).all()

    def get_permissions(self, *args, **kwargs):
        return IsAuthenticated(), IsSourceOwner()

    def retrieve(self, request, pk):
        instance = self.get_object()
        serializer = FilterSerializer(data=request.data, context={'name': instance.name})
        if not serializer.is_valid():
            return Response({
                'error': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        content = instance.content
        return Response({
            'content': ContentSerializer(content).data
        }, status=status.HTTP_200_OK)

    @action(methods=["POST"], detail=True, permission_classes=(IsAuthenticated, IsSourceOwner))
    def modify(self, request, pk):
        instance = self.get_object()
        text = request.data.get('content')
        if text is None:
            return Response({
                'errors': "content is required"
            }, status=status.HTTP_400_BAD_REQUEST)
        # 直接将内容放到数据库中，不修改文件
        content = instance.content
        content.content = text
        content.save()
        return Response({
            'status': 'success'
        }, status=status.HTTP_200_OK)
