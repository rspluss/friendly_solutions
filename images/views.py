from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from images.models import Image
from images.forms import AddImageForm
from images.serializers import ImageSerializer

from PIL import Image as ImageSize
from colorthief import ColorThief


def home(request):
    images = Image.objects.all()

    context = {'images': images}
    return render(request, "images/index.html", context)


def add_image(request):
    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')
        image_size = ImageSize.open(image)
        ct = ColorThief(image)
        dominant_color = ct.get_color(quality=1)

        add_new_image = Image.objects.create(
            title=data['title'],
            album=data['album'],
            width=image_size.size[0],
            height=image_size.size[1],
            color=dominant_color,
            image=image
        )
    form = AddImageForm()

    context = {'form': form}
    return render(request, "images/forms/add_image.html", context)


def delete_image(request, id_image):
    image = Image.objects.get(pk=id_image)
    image.delete()
    messages.success(request, "The photo has been correctly added")
    return redirect('images:home')


def update_image(request, id_image):
    image = Image.objects.get(pk=id_image)
    if request.method == "POST":
        form = AddImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, "The photo has been correctly updated")
    form = AddImageForm(instance=image)

    context = {'form': form}
    return render(request, "images/forms/edit_image.html", context)


@api_view(['GET', 'POST'])
def image_list_rest(request):
    if request.method == "GET":
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)