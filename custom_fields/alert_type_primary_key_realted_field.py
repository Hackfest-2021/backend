from collections import OrderedDict

from rest_framework import serializers

from alerts.models import AlertType


class AlertTypeField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        pk = super(AlertTypeField, self).to_representation(value)
        try:
            item = AlertType.objects.get(pk=pk)
            from alerts.serializers import AlertTypeSerializer
            serializer = AlertTypeSerializer(item)
            return serializer.data
        except AlertType.DoesNotExist:

            return None

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}

        return OrderedDict([(item.id, str(item)) for item in queryset])