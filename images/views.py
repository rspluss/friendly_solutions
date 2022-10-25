from django.shortcuts import render


def home(request):

    context = {}
    return render(request, "images/index.html", context)
