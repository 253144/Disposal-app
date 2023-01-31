from .models import Container, Price
from rest_framework import serializers


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class ContainerDetailSerializer(serializers.ModelSerializer):
    price = serializers.StringRelatedField()

    class Meta:
        model = Container
        fields = ['id', 'name', 'size', 'type', 'price']


class ContainerDefaultSerializer(serializers.ModelSerializer):
    price = serializers.PrimaryKeyRelatedField(
        queryset=Price.objects.all(), required=True)

    class Meta:
        model = Container
        fields = ['id', 'name', 'size', 'type', 'price']
