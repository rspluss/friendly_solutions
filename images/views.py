from django.shortcuts import render, redirect
from django.contrib import messages
from images.models import Image
from images.forms import AddImageForm


def home(request):
    images = Image.objects.all()

    context = {'images': images}
    return render(request, "images/index.html", context)


def add_image(request):
    if request.method == "POST":
        form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "The photo has been correctly added")
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
