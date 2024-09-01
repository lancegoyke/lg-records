from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import TextInput


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
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
