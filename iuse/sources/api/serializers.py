from rest_framework import serializers
from django.contrib.auth.models import User
from sources.models import Source
from accounts.api.serializers import UserSerializer
from rest_framework.exceptions import ValidationError
from utils.modelshelpers.enums import FileType
from sources.SourceServer import SourceServer
from utils.modelshelpers.enums import DeleteStatus
from recyclebin.models import Garbage


class SourceSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Source
        fields = ('id', 'name', 'owner', 'update_at', 'type')


class SourceWithChildrenSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    children = SourceSerializer(many=True)

    class Meta:
        model = Source
        fields = ('id', 'name', 'owner', 'children', 'update_at', 'type')


class SourceCreateDirSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, min_length=1)

    class Meta:
        model = Source
        fields = ('id', 'name')

    def validate(self, data):
        pk = self.context['pk']
        parent = Source.objects.filter(id=int(pk)).all()
        if not parent:
            raise ValidationError({'message': 'The dir does not exists'})
        if data['name'] in [child.name for child in parent[0].children]:
            raise ValidationError({'message': 'The dir has existed'})
        return data

    def create(self, validated_data):
        name = validated_data['name']
        pk = self.context['pk']
        owner = self.context['request'].user
        source = Source.objects.create(
            parent_dir_id=int(pk),
            owner=owner,
            name=name,
            type=FileType.DIR
        )
        SourceServer.create_sources(source)
        # SourceServer.create_sources_for_test(source)
        return source


class SourceDownloadSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, min_length=1)

    class Meta:
        model = Source
        fields = ('id', 'name')

    def validate(self, data):
        source = Source.objects.filter(name=data['name'], parent_dir_id=int(self.context['pk']))
        if not source or int(source[0].on_delete) == DeleteStatus.has_deleted:
            raise ValidationError('File does exist')
        data['path'] = SourceServer.generate_path(source[0])
        data['instance'] = source[0]
        return data


class SourceDeleteSerializer(SourceDownloadSerializer):
    pass


class SourceUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('id', 'name')

    def validate(self, data):
        if Source.objects.filter(name=data['name'], parent_dir_id=int(self.context['pk'])).exists():
            raise ValidationError({'message': f'{data["name"]} has exists'})