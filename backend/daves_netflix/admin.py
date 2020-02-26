from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(User, UserAdmin)
admin.site.register(StreamingService)
admin.site.register(StreamingAccount)
admin.site.register(UserStreamingAccount)
