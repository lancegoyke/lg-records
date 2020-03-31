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
    ordering = django_filters.OrderingFilter(
        choices=(
            ('-date_recorded', 'Newest First'),
            ('date_recorded', 'Oldest First'),
        ),
        fields = {
            'date_recorded': 'Date',
        }
    )

    class Meta:
        model = Record
        fields = {
            'time_score': ['lt', 'gt'],
        }