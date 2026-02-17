from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

NOT_ALLOWED_DOMAIN = [".ru", ".xyz"]

class UsuarioManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError("El correo electrónico no puede estar vacío")

        if "@" not in email:
            raise ValueError("Correo no válido")

        if any(domain in email for domain in NOT_ALLOWED_DOMAIN):
            raise ValueError("El dominio del correo no está permitido")

        if not password:
            raise ValueError("La contraseña no puede estar vacía")

        if len(password) < 6:
            raise ValueError("La contraseña debe tener mínimo 6 caracteres")

        if not any(c.isdigit() for c in password):
            raise ValueError("La contraseña debe tener al menos 1 número")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class UsuarioModel(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=50, unique=True)

    foto_perfil = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(max_length=250, blank=True)

    is_active = models.BooleanField(default=True)

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = "usuarios"
        ordering = ("-email",)
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.id} - {self.username} - {self.email}"

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = "Saitama"
        super().save(*args, **kwargs)