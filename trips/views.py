from django.shortcuts import render

# Create your views here.
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


class CreatePassengerTripAlertFeedBack(generics.ListCreateAPIView):
    queryset = PassengerAlerts.objects.all()
    serializer_class = PassengerAlertsSerializer
