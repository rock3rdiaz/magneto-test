from detector.models import Stats
from rest_framework import serializers


class StatsSerializer(serializers.ModelSerializer):
    """
    Stats serializer
    """
    class Meta:
        model = Stats
        exclude = ('id',)