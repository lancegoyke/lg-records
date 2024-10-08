from django.contrib import admin

from .models import Challenge, Record


# Register your models here.
class RecordInline(admin.TabularInline):
    model = Record


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    inlines = [
        RecordInline,
    ]
    list_display = (
        "name",
        "description",
        "date_created",
    )
