from rest_framework import serializers


class RecommendationSerializer(serializers.Serializer):
    length = serializers.FloatField(min_value=0)
    width = serializers.FloatField(min_value=0)
    height = serializers.FloatField(min_value=0)
    weight = serializers.FloatField(min_value=0)