from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StreamingAccountSerializer
from .models import StreamingAccount

class StreamingAccountView(viewsets.ModelViewSet):
    serializer_class = StreamingAccountSerializer
    queryset = StreamingAccount.objects.all()
