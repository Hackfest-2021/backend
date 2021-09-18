from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from account.models import Account
from alerts.serializers import AlertSerializer
from custom_fields.account_type_related_field import AccountTypeField
from custom_fields.trip_alert_primary_related_field import TripAlertPrimaryKeyRealtedField
from custom_fields.trip_primary_key_related_field import TripTypeField
from trips.models import Trips, TripPassengers, TripAlerts, PassengerAlerts


class TripSerializer(serializers.ModelSerializer):
    driver = AccountTypeField(read_only=False, queryset=Account.objects.all())

    class Meta:
        model = Trips
        fields = '__all__'
        depth = 1

class TripPassengerSerializer(serializers.ModelSerializer):
    passenger = AccountTypeField(read_only=False, queryset=Account.objects.all())
    trip = TripTypeField(read_only=False,queryset=Trips.objects.all())
    class Meta:
        model = TripPassengers
        fields = '__all__'
        depth = 1

class TripAlertsSerializer(WritableNestedModelSerializer):

    alert = AlertSerializer(read_only=False)
    trip = TripTypeField(read_only=False,queryset=Trips.objects.all())

    class Meta:
        model = TripAlerts
        fields = '__all__'
        depth = 2


class PassengerAlertsSerializer(WritableNestedModelSerializer):
    trip_alert = TripAlertPrimaryKeyRealtedField(read_only=False,queryset=TripAlerts.objects.all())
    passenger = AccountTypeField(read_only=False, queryset=Account.objects.all())

    class Meta:
        model = PassengerAlerts
        fields = '__all__'
        depth = 1