from .models import Client, Address
from rest_framework import serializers


class ClientDetailSerializer(serializers.ModelSerializer):
    address = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = ['id', 'name', 'lname', 'phone', 'address']


class ClientDefaultSerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(), required=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'lname', 'phone', 'address']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'house', 'apart', 'zip', 'city']
