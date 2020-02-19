from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=100, default="", null=False)
    handle = models.CharField(max_length=30)
    avatar_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StreamingService(models.Model):
    name = models.CharField(max_length=30)
    logo_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StreamingAccount(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    streaming_service = models.ForeignKey(StreamingService, on_delete=models.CASCADE)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    spots = models.IntegerField()
    price = models.IntegerField()
    four_k = models.BooleanField(default=False)
    users = models.ManyToManyField(User, through="UserStreamingAccount")

    def __str_(self):
        return self.name

class UserStreamingAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    streaming_account = models.ForeignKey(StreamingAccount, on_delete=models.CASCADE)

    def __str_(self):
        return self.name
