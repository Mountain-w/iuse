from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, min_length=4)
    password = serializers.CharField(min_length=6, max_length=20)
    class Meta:
        model = User
        fields = ('username', "password")


class SignupSerializer(LoginSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def validate(self, data):
        username = data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError({"message" :"User is already exists"})
        if User.objects.filter(email=data['email'].lower()).exists():
            raise ValidationError({"message":"The email has been registered"})
        return data

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        user.profile
        return user
