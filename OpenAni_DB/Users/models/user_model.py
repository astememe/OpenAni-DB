from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
# class UsuarioManager(BaseUserManager):
# Lógica de verificación (Fabio)

class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None,**extra_fields):
        if not email:
            raise ValueError("El correo electrónico no puede estar vacío")

        # for domain in NOT_ALLOWED_DOMAIN:
        #     if domain in email:
        #         raise ValueError("El dominio del correo no está permitido")

        if not password:
            raise ValueError("Password can't be empty")

        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long")

        if not any(caracter.isdigit() for caracter in password):
            raise ValueError("Password must contain at least one digit")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)


        return self.create_user(email, password, **extra_fields)



class UserModel(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True, null= False, blank=False, verbose_name="usuario")
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False, verbose_name="Correo electrónico", help_text="(Obligatorio)")
    imagen = models.CharField(null=False, blank=False)
    descripcion = models.TextField(max_length=350, default="Escriba su nueva descripción")
    is_superuser = models.BooleanField(default=False, verbose_name="¿Es super usuario?")
    is_staff = models.BooleanField(default=False, verbose_name="Es staff?")
    # objects = UsuarioManager()

    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "usuarios"
        ordering = ("-email",)
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"[{self.id}] - {self.username} - {self.email}"

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = "Saitama"
        super().save(*args, **kwargs)