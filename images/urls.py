from django.urls import path
from images import views

app_name = "images"

urlpatterns = [
    path("", views.home, name="home"),
]