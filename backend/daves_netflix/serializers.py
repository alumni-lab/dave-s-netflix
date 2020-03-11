from rest_framework import serializers
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
