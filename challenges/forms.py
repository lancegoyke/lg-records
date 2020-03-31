from django.forms import ModelForm

from .models import Record

class RecordCreateForm(ModelForm):
    class Meta:
        model = Record
        fields = ['time_score', 'notes',]