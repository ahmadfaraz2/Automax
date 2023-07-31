import django_filters

from .models import Listing


class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Listing
        fields = {
            "brands": ["exact"],  # It says I want "exact" match for "brands" field.
            "transmission": ["exact"],
            "mileage": ["lt"],
            "model": ["icontains"],
        }  # Fields on which filter(django_filters) can filter upon.
