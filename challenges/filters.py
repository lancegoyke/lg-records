from django.contrib.auth import get_user_model
from django import forms

import django_filters

from .models import Challenge, Record

class ChallengeFilter(django_filters.FilterSet):
    ordering = django_filters.OrderingFilter(
        choices=(
            ('-date_created', 'Newest First'),
            ('date_created', 'Oldest First'),
        ),
        fields = {
            'date_created': 'Date',
        }
    )

    class Meta:
        model = Challenge
        fields = {
            'name': ['icontains'],
        }


class RecordFilter(django_filters.FilterSet):
    order = django_filters.OrderingFilter(
        label="Sort",
        choices=(
            ('time', 'Fastest'),
            ('-time', 'Slowest'),
            ('-when', 'Newest'),
            ('when', 'Oldest'),
        ),
        fields = (
            ('date_recorded', 'when'),
            ('time_score', 'time'),
        ),
        field_labels = {
            'date_recorded': 'Oldest',
            '-date_recorded': 'Newest',
            'time_score': 'Fastest',
            '-time_score': 'Slowest',
        }
    )

    class Meta:
        model = Record
        fields = []
            