import generics as generics
from django.shortcuts import render
from rest_framework import status, generics, permissions, mixins

# Create your views here.
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny

from alerts.models import Alerts
from alerts.serializers import AlertSerializer

class AlertCreateList(generics.ListCreateAPIView):
    # permission_classes = (CsrfExemptSessionAuthentication,AllowAny,)
    queryset = Alerts.objects.all()
    serializer_class = AlertSerializer