import generics as generics
from django.shortcuts import render
from rest_framework import status, generics, permissions, mixins

# Create your views here.
from alerts.models import Alerts
from alerts.serializers import AlertSerializer


class AlertCreateList(generics.ListCreateAPIView):
    queryset = Alerts.objects.all()
    serializer_class = AlertSerializer