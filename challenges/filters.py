import django_filters

from .models import Challenge

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