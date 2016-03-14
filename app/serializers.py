from rest_framework import serializers


class MouseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
