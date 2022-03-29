from rest_framework import serializers
from sources.models import Source
from sources.api.serializers import SourceSerializer
from recyclebin.models import Garbage
from recyclebin.RecyclebinServer import RecyclebinServer


class GarbageSerializer(serializers.ModelSerializer):
    source = SourceSerializer()
    rest_time = serializers.SerializerMethodField()

    class Meta:
        model = Garbage
        fields = ('id', 'source', 'rest_time')

    def get_rest_time(self, obj):
        return RecyclebinServer.get_rest_minute(obj)