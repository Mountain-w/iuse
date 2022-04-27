from rest_framework import serializers
from editor.models import Content
from sources.api.serializers import SourceSerializer
from sources.models import Source
from rest_framework.exceptions import ValidationError


class ContentSerializer(serializers.ModelSerializer):
    file = SourceSerializer()

    class Meta:
        model = Content
        fields = ('file', 'content',)


class FilterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = ('id',)

    def check_type(self, name):
        import re
        pattern = re.compile(r".+\.(?:txt|md|py|js)")
        result = re.findall(pattern, name)
        if not result:
            return False
        return True

    def validate(self, data):
        name = self.context['name']
        if not self.check_type(name):
            raise ValidationError({"message": f'[{name}]---The type doesn\'t export now'})
        return data

