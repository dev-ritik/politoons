from rest_framework import serializers
from .models import Politoon


class ToonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Politoon
        fields = ("name", "majorRole", "party")
