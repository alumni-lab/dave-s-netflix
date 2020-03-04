from django.db import models
from django.contrib.auth.models import User


class StreamingService(models.Model):
    name = models.CharField(max_length=30)
    logo_url = models.CharField(max_length=100)


class StreamingAccount(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    streaming_service = models.ForeignKey(StreamingService, on_delete=models.CASCADE)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    spots = models.IntegerField()
    price = models.IntegerField()
    four_k = models.BooleanField(default=False)
    users = models.ManyToManyField(User, through="UserStreamingAccount", related_name="users")


class UserStreamingAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    streaming_account = models.ForeignKey(StreamingAccount, on_delete=models.CASCADE)
