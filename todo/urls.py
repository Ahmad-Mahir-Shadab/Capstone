from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('del/<str:item_id>', views.remove, name="remove"),
    path('create', views.create, name="create"),
    path("form", views.form, name="form"),
    path("notes/<str:filename>", views.filename, name="filename"),
    path("edit/<str:postId>", views.edit, name="edit")
]
