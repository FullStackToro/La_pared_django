from django.urls import path, include
from . import views

urlpatterns = [
    path("<op>", views.success),
    path("", views.muro),
    path("add_mensaje/<_op>", views.mensaje),
    path("add_comentario/<_op>/<_mensaje_id>", views.comentario),
    path("eliminar_comentario/<_op>/<_comentario_id>", views.delete_comment),
    path("eliminar_mensaje/<_op>/<_mensaje_id>", views.delete_mensaje)
]
