from django.db import models

class Mensajes(models.Model):
    mensaje = models.TextField()
    mensaje_usuario_id = models.ForeignKey('login_app.Usuario', related_name="users_mensaje", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comentarios(models.Model):
    comentario = models.TextField()
    comentario_mensaje_id = models.ForeignKey(Mensajes, related_name="mensaje_comentario", on_delete=models.CASCADE)
    comentario_usuario_id = models.ForeignKey('login_app.Usuario', related_name="users_comentario", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
