from django.contrib import admin

# Register your models here.
from .models import User, UserDetail

admin.site.register(User)
admin.site.register(UserDetail)
