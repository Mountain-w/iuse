from rest_framework import serializers
from editor.models import Content
from sources.api.serializers import SourceSerializer


class ContentSerializer(serializers.ModelSerializer):
    file = SourceSerializer()

    class Meta:
        model = Content
        fields = ('file', 'content',)
