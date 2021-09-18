from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from trips.models import Trips, TripPassengers, TripAlerts, PassengerAlerts
from trips.serializers import TripSerializer, TripPassengerSerializer, TripAlertsSerializer, PassengerAlertsSerializer


class CreateListTrips(generics.ListCreateAPIView):
    queryset = Trips.objects.all()
    serializer_class = TripSerializer



class CreateTripPassenger(generics.ListCreateAPIView):

    queryset = TripPassengers.objects.all()
    serializer_class = TripPassengerSerializer

class CreateTripAlert(generics.ListCreateAPIView):
    queryset = TripAlerts.objects.all()
    serializer_class = TripAlertsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['alert__alert_type__id']
    #
    # def create(self, request, *args, **kwargs):
    #     TripAlerts.objects.filter(alert__alert_type__id=)


class CreatePassengerTripAlertFeedBack(generics.ListCreateAPIView):
    queryset = PassengerAlerts.objects.all()
    serializer_class = PassengerAlertsSerializer
