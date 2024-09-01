from django.forms import ModelForm, TextInput

from .models import Challenge, Record


class ChallengeCreateForm(ModelForm):
    class Meta:
        model = Challenge
        fields = [
            "name",
            "description",
            "tags",
        ]
        widgets = {"tags": TextInput(attrs={"class": "input"})}


class RecordCreateForm(ModelForm):
    class Meta:
        model = Record
        fields = [
            "time_score",
            "notes",
        ]
