from rest_framework import viewsets, status
from recyclebin.models import Garbage
from recyclebin.api.serializers import GarbageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from recyclebin.RecyclebinServer import RecyclebinServer
from utils.modelshelpers.enums import DeleteStatus
from utils.permissions import IsSourceOwner


class GarbageViewSet(viewsets.GenericViewSet):
    serializer_class = GarbageSerializer
    permission_classes = (IsAuthenticated, IsSourceOwner)
    queryset = RecyclebinServer.get_query_set()

    def list(self, request):
        query_set = RecyclebinServer.get_query_set(request.user)
        return Response({
            'garbages': GarbageSerializer(query_set, many=True).data
        }, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True)
    def recover(self, request, pk):
        """
        从回收站中恢复
        """
        self.get_queryset()
        instance = self.get_object()
        source = instance.source
        source.on_delete = DeleteStatus.exists
        source.save()
        instance.delete()
        return Response({'success': "ok"})