from rest_framework import viewsets, status
from recyclebin.models import Garbage
from recyclebin.api.serializers import GarbageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class GarbageViewSet(viewsets.GenericViewSet):
    serializer_class = GarbageSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        query_set = Garbage.objects.filter(owner=request.user).all()
        return Response({
            'garbages': GarbageSerializer(query_set, many=True).data
        }, status=status.HTTP_200_OK)
