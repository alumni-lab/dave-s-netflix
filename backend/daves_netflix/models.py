from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Create a custom User based on the built-in User model allowing future customization
    pass


class StreamingService(models.Model):
    name = models.CharField(max_length=30)
    logo_url = models.CharField(max_length=100)


class StreamingAccount(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="owner")
    streaming_service = models.ForeignKey(StreamingService, on_delete=models.CASCADE)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    spots = models.IntegerField()
    price = models.IntegerField()
    four_k = models.BooleanField(default=False)
    users = models.ManyToManyField(User, through="UserStreamingAccount", related_name="users")


class UserStreamingAccount(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    streaming_account = models.ForeignKey(StreamingAccount, on_delete=models.CASCADE)
