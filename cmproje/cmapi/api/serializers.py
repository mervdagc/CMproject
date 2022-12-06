from rest_framework import serializers

from .models import Apimodel


class ApimodelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    phone_number = serializers.CharField()
    country = serializers.CharField()
    operator = serializers.CharField()

    def create(self, validated_data):
        print(validated_data)
        return Apimodel.objects.create(**validated_data)
        pass

    def update(self, instance, validated_data):
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.country = validated_data.get('country', instance.country)
        instance.operator = validated_data.get('operator', instance.operator)
        instance.save()
