from rest_framework import serializers
from django.contrib.auth.models import User
from .models import StreamingAccount

class StreamingAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingAccount
        fields = (
            "id",
            "owner",
            "streaming_service",
            "login",
            "password",
            "spots",
            "price",
            "four_k",
            "users"
        )
        depth = 1

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
