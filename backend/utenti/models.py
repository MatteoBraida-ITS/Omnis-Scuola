from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# Create your models here.
class UtenteManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra):
        if not email:
            raise ValueError("L'email è obbligatoria")
        email = email.strip().lower()
        user = self.model(email=email, **extra)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra):
        extra.setdefault("is_staff", False)
        extra.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra)

    def create_superuser(self, email, password=None, **extra):
        extra.setdefault("is_staff", True)
        extra.setdefault("is_superuser", True)
        extra.setdefault("ruolo", Utente.Ruolo.DIRETTORE)
        return self._create_user(email, password, **extra)


class Utente(AbstractUser):
    class Ruolo(models.TextChoices):
        DIRETTORE = "DIRETTORE", "Direttore"
        SEGRETERIA = "SEGRETERIA", "Segreteria"
        DOCENTE = "DOCENTE", "Docente"
        STUDENTE = "STUDENTE", "Studente"

    username = None
    email = models.EmailField("email", unique=True)
    ruolo = models.CharField(max_length=20, choices=Ruolo.choices)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "ruolo"]

    objects = UtenteManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.strip().lower()
        super().save(*args, **kwargs)
