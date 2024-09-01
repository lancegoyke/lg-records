import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    class Sex(models.TextChoices):
        UNKNOWN = "U", _("Prefer not to say")
        FEMALE = "F", _("Female")
        MALE = "M", _("Male")

    sex = models.CharField(max_length=1, choices=Sex.choices, default=Sex.UNKNOWN)
    birthday = models.DateField(
        help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
        blank=True,
        null=True,
    )
    points = models.PositiveIntegerField(default=0)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("user_detail")
