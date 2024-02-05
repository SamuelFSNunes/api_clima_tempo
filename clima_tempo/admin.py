from django.contrib import admin
from .models.ModelEntity import ModelEntity
from .models.ModelUser import ModelUser

# Register your models here.

admin.site.register(ModelEntity)
admin.site.register(ModelUser)