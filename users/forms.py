from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import TextInput

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = (
            "email",
            "username",
            "birthday",
            "sex",
        )
        widgets = {
            "email": TextInput(attrs={"class": "input"}),
            "birthday": TextInput(attrs={"class": "input"}),
        }
