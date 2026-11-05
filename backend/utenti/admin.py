from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UtenteChangeForm, UtenteCreationForm
from .models import Utente


# Register your models here.
@admin.register(Utente)
class UtenteAdmin(UserAdmin):
    add_form = UtenteCreationForm
    form = UtenteChangeForm
    model = Utente

    list_display = ("email", "first_name", "last_name", "ruolo", "is_active")
    list_filter = ("ruolo", "is_active", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Dati personali", {"fields": ("first_name", "last_name", "ruolo")}),
        (
            "Permessi",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Date", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "ruolo",
                    "usable_password",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
