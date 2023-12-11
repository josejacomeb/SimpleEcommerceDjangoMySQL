from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("anadir/<str:nombre>", views.anadir, name="anadir"),
    path("editar/<str:nombre>/<int:id>/", views.editar, name="editar"),    
    path("eliminar/<str:nombre>/<int:id>/", views.eliminar, name="eliminar"),
]