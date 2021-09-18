from rest_framework import serializers

from alerts.models import Alerts


class AlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alerts
        fields = '__all__'
        depth = 1

