from marina.power.models import Boat, Engine, BoatEngine
from rest_framework import serializers


class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = [
            "id",
            "manufacturer",
            "model_name",
            "model_year",
            "custom_description",
            "price",
            "hull_number",
            "engines",
        ]


class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = [
            "id",
            "manufacturer",
            "model_name",
            "model_year",
            "custom_description",
            "price",
            "serial_number",
            "hours_of_operation",
            "boats",
        ]


class BoatEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoatEngine
        fields = ["id", "boat", "engine", "date_attached", "date_removed"]
