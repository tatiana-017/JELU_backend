from django.contrib import admin
from .models.user import User
from .models.video import Video

# Register your models here.
admin.site.register(User)
admin.site.register(Video)