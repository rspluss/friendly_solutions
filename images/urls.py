from django.urls import path
from images import views

app_name = "images"

urlpatterns = [
    path("", views.home, name="home"),
    path('add_image/', views.add_image, name="add_image"),
    path('update_image/<str:id_image>/', views.update_image, name="update_image"),
    path('detele_image/<str:id_image>/', views.delete_image, name="delete_image"),
]
