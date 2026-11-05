from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm
from .models import Utente


class UtenteCreationForm(AdminUserCreationForm):
    class Meta:
        model = Utente
        fields = ("email", "first_name", "last_name", "ruolo")


class UtenteChangeForm(UserChangeForm):
    class Meta:
        model = Utente
        fields = ("email", "first_name", "last_name", "ruolo")
