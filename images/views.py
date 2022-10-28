from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.core.files.base import ContentFile
from django.core.paginator import Paginator

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from images.models import Image
from images.forms import AddImageForm, UpdateImageForm
from images.serializers import ImageSerializer

from PIL import Image as ImageSize
from colorthief import ColorThief

import requests
import ast


def home(request):
    images = Image.objects.all().order_by('-id')

    #Set up Pagination
    p = Paginator(images, 20)
    page = request.GET.get('page')
    images_p = p.get_page(page)

    context = {'images': images, 'images_p': images_p}
    return render(request, "images/index.html", context)


def add_image(request):
    if request.method == "POST":
        data = request.POST
        image_url = data['url']
        image_name = image_url.split("/")[-1]
        response = requests.get(image_url)
        obj = Image()
        obj.image.save(image_name, ContentFile(response.content), save=False)

        image_size = ImageSize.open(obj.image)
        ct = ColorThief(obj.image)
        dominant_color = ct.get_color(quality=1)

        obj.title = data['title']
        obj.albumId = data['albumId']
        obj.width = image_size.size[0],
        obj.height = image_size.size[1],
        obj.color = dominant_color,
        obj.save()
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
        form = UpdateImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, "The photo has been correctly updated")
    form = UpdateImageForm(instance=image)

    context = {'form': form}
    return render(request, "images/forms/edit_image.html", context)


@api_view(['GET', 'POST'])
def image_list_rest(request):
    if request.method == "GET":
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        data = request.data
        for n in range(len(data)):
            image_url = data[n]['url']
            image_name = image_url.split("/")[-1]
            response = requests.get(image_url + ".jpg")
            obj = Image()
            obj.image.save(image_name, ContentFile(response.content), save=False)

            image_size = ImageSize.open(obj.image)
            ct = ColorThief(obj.image)
            dominant_color = ct.get_color(quality=1)

            obj.title = data[n]['title']
            obj.albumId = data[n]['albumId']
            obj.width = image_size.size[0],
            obj.height = image_size.size[1],
            obj.color = dominant_color,
            obj.save()

        return Response(status=status.HTTP_201_CREATED)


def image_list_json_file(request):
    with open("static/photos.txt") as f:
        files = ast.literal_eval(f.read())

    for index in range(len(files)):
        for key in files[index]:
            print(files[index][key])

        image_url = files[index]['url']
        image_name = image_url.split("/")[-1]
        response = requests.get(image_url + ".jpg")
        obj = Image()
        obj.image.save(image_name, ContentFile(response.content), save=False)

        image_size = ImageSize.open(obj.image)
        ct = ColorThief(obj.image)
        dominant_color = ct.get_color(quality=1)

        obj.title = files[index]['title']
        obj.albumId = files[index]['albumId']
        obj.width = image_size.size[0],
        obj.height = image_size.size[1],
        obj.color = dominant_color,
        obj.save()

    context = {}
    return render(request, "images/index.html", context)
