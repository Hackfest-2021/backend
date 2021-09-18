from collections import OrderedDict

from rest_framework import serializers

from trips.models import Trips


class TripTypeField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        pk = super(TripTypeField, self).to_representation(value)
        try:
            item = Trips.objects.get(pk=pk)
            from trips.serializers import TripSerializer
            print("sss")
            serializer = TripSerializer(item)
            return serializer.data
        except Trips.DoesNotExist:

            return None

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}

        return OrderedDict([(item.id, str(item)) for item in queryset])