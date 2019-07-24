from rest_framework import serializers
from .models import *

class UserDetailSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=25)
    photo = serializers.CharField(max_length=50)
    id_usertype = serializers.CharField(max_length=10)
    user_type = serializers.CharField(max_length=50)
    status =  serializers.CharField(max_length=10)

class UserDetailTokenSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=30)
    token = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=25)
    photo = serializers.CharField(max_length=50)
    user_type = serializers.CharField(max_length=50)
    status =  serializers.CharField(max_length=10)

class UserSelect(serializers.Serializer):
    id = serializers.CharField(max_length=10)
    first_name = serializers.CharField(max_length=50)

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'

class UserTypeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ("status", "last_updated",)

class UserTypeSelectComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ("status", "last_updated",)