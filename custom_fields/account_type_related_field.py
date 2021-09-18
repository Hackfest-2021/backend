from collections import OrderedDict

from rest_framework import serializers

from account.models import Account
from account.serializers import AccountSerializer
from trips.models import Trips
class AccountTypeField(serializers.RelatedField):

    def get_queryset(self):
        return Account.objects.all()

    def to_representation(self, instance):
        return AccountSerializer(instance).data

    def to_internal_value(self, data):
        print(data)
        # inventor = data.get('inventor', None)
        try:
            user = Account.objects.get(username=data)
        except Account.DoesNotExist:
            raise serializers.ValidationError('bad driver')
        return user
