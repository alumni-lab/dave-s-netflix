from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StreamingAccountSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import StreamingAccount

class StreamingAccountView(viewsets.ModelViewSet):
    serializer_class = StreamingAccountSerializer
    queryset = StreamingAccount.objects.all()


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
