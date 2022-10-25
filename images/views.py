from django.shortcuts import render
from images.models import Image


def home(request):
    images = Image.objects.all()

    context = {'images': images}
    return render(request, "images/index.html", context)
