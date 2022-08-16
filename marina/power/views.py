from django.shortcuts import render

from marina.power.models import Boat, Engine, BoatEngine
from marina.power.serializers import (
    BoatSerializer,
    EngineSerializer,
    BoatEngineSerializer,
)
from rest_framework import generics


class BoatList(generics.ListCreateAPIView):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer


class BoatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer


class EngineList(generics.ListCreateAPIView):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer


class EngineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer


class BoatEngineList(generics.ListCreateAPIView):
    queryset = BoatEngine.objects.all()
    serializer_class = BoatEngineSerializer


class BoatEngineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoatEngine.objects.all()
    serializer_class = BoatEngineSerializer
