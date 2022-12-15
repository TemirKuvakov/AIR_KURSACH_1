from rest_framework import serializers


class MatrixSerializer(serializers.Serializer):
    size = serializers.IntegerField()
    matrix = serializers.ListField(child=serializers.ListField(child=serializers.FloatField()))
    count = serializers.ListField()
    vec = serializers.ListField(child=serializers.ListField(child=serializers.FloatField()))
