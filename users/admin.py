from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "points",
        "birthday",
        "sex",
    ]
    fieldsets = (
        (None, {"fields": ("username",)}),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "email", "birthday", "sex")},
        ),
        (
            _("Permissions"),
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
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Scoping"), {"fields": ("points",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     if db_field.name == "password":
    #         kwargs["widget"] = PasswordInput(attrs={"autocomplete": "new-password"})
    #     return super().formfield_for_dbfield(db_field, **kwargs)
