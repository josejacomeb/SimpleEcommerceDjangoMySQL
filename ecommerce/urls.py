from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("anadir_tv", views.anadir_tv, name="anadir_tv"),
    path("editar_tv/<int:tv_id>/", views.editar_tv, name="editar_tv"),    
    path("eliminar/<int:tv_id>/", views.eliminar, name="eliminar"),
]