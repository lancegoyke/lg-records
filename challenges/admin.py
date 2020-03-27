from django.contrib import admin

from .models import Challenge, Record

# Register your models here.
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created',)

admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Record)