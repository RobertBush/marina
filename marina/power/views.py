from marina.power.models import Boat, Engine, BoatEngine
from marina.power.serializers import (
    BoatSerializer,
    EngineSerializer,
    BoatEngineSerializer,
)
from rest_framework.viewsets import ModelViewSet


class BoatViewSet(ModelViewSet):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer


class EngineViewSet(ModelViewSet):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer


class BoatEngineViewSet(ModelViewSet):
    queryset = BoatEngine.objects.all()
    serializer_class = BoatEngineSerializer
