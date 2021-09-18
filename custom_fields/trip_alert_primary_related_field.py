from collections import OrderedDict

from rest_framework import serializers

from trips.models import TripAlerts


class TripAlertPrimaryKeyRealtedField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        pk = super(TripAlertPrimaryKeyRealtedField, self).to_representation(value)
        try:
            item = TripAlerts.objects.get(pk=pk)
            from trips.serializers import TripAlertsSerializer
            serializer = TripAlertsSerializer(item)
            return serializer.data
        except TripAlerts.DoesNotExist:

            return None

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}

        return OrderedDict([(item.id, str(item)) for item in queryset])