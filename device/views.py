from django.shortcuts import render

# Create your views here.
from djangochannelsrestframework.consumers import AsyncAPIConsumer
from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.observer import model_observer
from rest_framework import status

from trips.models import Trips
from trips.serializers import TripSerializer


class StreamConsumer(AsyncAPIConsumer):
    lookup_field = 'id'
    queryset = Trips.objects.all()
    serializer_class = TripSerializer

    @model_observer(Trips)
    async def DeviceSettings_activity(self, message: TripSerializer, observer=None, **kwargs):
        await self.send_json(message.data)

    @DeviceSettings_activity.serializer
    def DeviceSettings_activity(self, instance: Trips, action, **kwargs) -> TripSerializer:
        '''This will return the comment serializer'''
        return TripSerializer(instance)

    @action()
    async def subscribe_to_DeviceSettings(self, **kwargs):
        print("ssss")
        await self.DeviceSettings_activity.subscribe()