import generics as generics
from django.shortcuts import render
from rest_framework import status, generics, permissions, mixins

# Create your views here.
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from alerts.models import Alerts, AlertType
from alerts.serializers import AlertSerializer, AlertTypeSerializer


class AlertCreateList(generics.ListCreateAPIView):
    # permission_classes = (CsrfExemptSessionAuthentication,AllowAny,)
    queryset = Alerts.objects.all()
    serializer_class = AlertSerializer

@api_view(["GET"])
def alert_types(request):

    return Response({"alert_types": AlertTypeSerializer(AlertType.objects.all(),many=True).data})