from .models import Order, OrderList
from rest_framework import serializers

from clients.models import Client
from clients.serializers import ClientDetailSerializer

from offer.serializers import ContainerDetailSerializer
from offer.models import Container


class OrderDetailSerializer(serializers.ModelSerializer):
    client = ClientDetailSerializer()

    class Meta:
        model = Order
        fields = ['id', 'order_status', 'payment_status',
                  'order_date', 'collect_date', 'client']


class OrderDefaultSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=True)

    class Meta:
        model = Order
        fields = ['id', 'order_status', 'payment_status',
                  'order_date', 'collect_date', 'client']


class OrderListDetailSerializer(serializers.ModelSerializer):
    order = OrderDetailSerializer()
    container = ContainerDetailSerializer()

    class Meta:
        model = OrderList
        fields = ['id', 'order', 'container']


class OrderListDefaultSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(), required=True)
    container = serializers.PrimaryKeyRelatedField(
        queryset=Container.objects.all(), required=True)

    class Meta:
        model = OrderList
        fields = ['id', 'order', 'container']
