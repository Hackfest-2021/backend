import base64

import numpy
from django.shortcuts import render

# Create your views here.
from djangochannelsrestframework.consumers import AsyncAPIConsumer
from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.observer import model_observer
from rest_framework import status

from trips.models import Trips
from trips.serializers import TripSerializer

from PIL import Image
import io
import PIL.Image as Image
import cv2
def stringToImage(base64_string):
    imgdata = base64.b64decode(base64_string)
    return Image.open(io.BytesIO(imgdata))
count=0

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
        global count
        print("ssss")
        print(kwargs)
        img_str = kwargs.get('data')
        # print(type(img_str))
        # print(img_str)
        if img_str:
            image = stringToImage(img_str)
            print(type(image))
            open_cv_image = numpy.array(image)
            cv2.imwrite(f'{count}.jpg',open_cv_image)
            # count= count + 1
            # cv2.imwrite('sss.png', image)        # print(kwargs['data'])
        await self.DeviceSettings_activity.subscribe()