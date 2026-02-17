from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# class UsuarioManager(BaseUserManager):
# Lógica de verificación (Fabio)

class UserModel(PermissionError, AbstractBaseUser):
    usuario = models.CharField(max_length=15, unique=True, null= False, blank=False, verbose_name="usuario")
    correo = models.EmailField(max_length=100, unique=True, null=False, blank=False, verbose_name="Correo electrónico", help_text="(Obligatorio)")
    # Fabio, cambia lo que gustes en contraseña
    contrasena = models.TextField(min_length=6, unique=True, null=False, blank=False, help_text="(Obligatorio)")
    imagen = models.TextField()
    descripcion = models.TextField(max_length=350)
    es_superusuario = models.BooleanField(default=False, verbose_name="¿Es super usuario?")

    # Fabio, con objects pordrás llamar a la verificación de usuario
    # objects = UsuarioManager()

    USERNAME_FIELD = "correo"
    REQUIRED_FIELDS = ["usuario", "contrasena"]

    class Meta:
        db_table = "usuarios"
        ordering = ("-correo",)
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"[{self.id}] - {self.usuario} - {self.correo}"

    def save(self, *args, **kwargs):
        if not self.usuario:
            self.usuario = "Saitama"
        super().save(*args, **kwargs)