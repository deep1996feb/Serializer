from rest_framework import serializers

class StudentsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    address = serializers.CharField(max_length=100)