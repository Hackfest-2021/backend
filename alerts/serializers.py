from rest_framework import serializers

from alerts.models import Alerts, AlertType
from custom_fields.alert_type_primary_key_realted_field import AlertTypeField


class AlertTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertType
        fields = '__all__'
        depth = 1


class AlertSerializer(serializers.ModelSerializer):
    alert_type = AlertTypeField(read_only=False, queryset=AlertType.objects.all())

    class Meta:
        model = Alerts
        fields = '__all__'
        depth = 1
