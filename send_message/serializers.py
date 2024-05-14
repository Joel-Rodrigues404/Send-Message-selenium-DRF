from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    message = serializers.CharField(max_length=500)
