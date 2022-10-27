from django.contrib import admin
from images.models import Image, Album


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'albumId', 'width', 'height', 'color', 'image', 'url']

